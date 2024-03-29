import EnumTypes
import BaseClass
import TSModel
from EnumTypes import FMsg as msg
import threading
import time

class TSOTM(BaseClass.TBaseClass):
    # ------------------------ VARIABLES ------------------------ 
    # upon creation an instance object of TSOTM class, its MsgToSGMM variable has to be assigned to SGMM.ProcessMsg() method
    # this way the TSOTM object can send messages to a TSGMM object
    MsgToSGMM = None
    
    # this is the trading simulation model
    TSM = TSModel.TTSModel()
    
    # Trading Signal File, in this implementation we will use lists, not the memory mapped files
    # CASM will be building this list and sending to SOTM for analysis
    TSF = []
    
    # Trades Details File, this file (list) is written by the TSM model and contains the results
    # of simulated trading entries on the current history DPP file. This will show when a given trade 
    # was made, how big was it, when it was closed and profit/loss amount
    TDF = []
    
    # Data Pipe File, raw trading history file/list. It is provided by CASM
    DPF = []
    
    # Model Variables File, all variables for the current implementation
    MVF = []        
    
    # ------------------------ METHODS ------------------------ 
    # Load settings
    def LoadSettings(self):
        sett = None  # file variable 
        
        # here settSOTM.ini to be opened and parameter to be read
        try:
            sett = open('settSOTM.ini')
            
            
            sett.close()
        except:
            return False
        return True
        
    # Init any starting state
    def __init__(self, _FErrorLogFName, _FEventLongName):
        super().__init__(_FErrorLogFName, _FEventLongName)  # call parent method inherited init first
        # read all settings for this optimization
        if not self.LoadSettings:
            self.LogError("Error while loading settings")
        # start self.Poll as a thread, it will be periodically checking for any pending messagges to serve
        thread = threading.Thread(target=self.Poll, args=())
        thread.daemon = True                            
        thread.start()

    def Poll(self):
        # this will be polling the RecMsg variable that contains an unprocessed message
        while True:
            # CASM gave us results, start virtual trading simulation
            if self.RecMsg == msg.PM_CASM_READY:
                # test the obtained TSF in virtual trading on the given history DPP
                self.TSM.RunModel(self.DPF, self.TSF, self.TDF, self.MVF)
                self.Log(0, 'SOTM finished')
                # once finished, the model will generate TDF list which we need to pass further to SGMM for 
                # analysis
                self.MsgToSGMM(msg.PM_SOTM_READY, self.TDF)
                self.RecMsg = None
            else:   
                time.sleep(0.01)
        
    # The base functionality class declares the message-type interaction between the instances of different classes
    # The parent class shall implement its way of processing of the received messages
    #   enum parameter is the Message it has received, see EnumTypes.py
    #   param is any parameter a particular meggase may be accompanied with
    def ProcessMsg(self, enum, param, param2, param3):
        # initialize 
        if  enum == msg.PM_INIT:
            # do init. Note: in python __init__ is automatically called upon creating a class instance.
            # just in case we need to re-init, keep  this message
            __init__(self, "SOTMerr.log")
            
        # return last error
        elif enum == msg.PM_GETLASTERROR:
            return self.FLastError
            
        # CASM gave us results, start virtual trading simulation
        elif enum == msg.PM_CASM_READY:
            # by now, CASM should have finished writting into TSF and we ready to simulate trading
            # on the given history DPF. For this message param points to the CASM's TSF list
            self.TSF = param
            # update addres of DPF
            self.DPF = param2
            # update address of MVF
            self.MVF = param3
            # to avoid recursion just record the message we received and return. The rest will be handled by self.Poll()
            self.RecMsg = enum
            
        