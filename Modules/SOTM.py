import EnumTypes
import BaseClass
import TSModel
from EnumTypes import FMsg as msg

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
            
    # The base functionality class declares the message-type interaction between the instances of different classes
    # The parent class shall implement its way of processing of the received messages
    #   enum parameter is the Message it has received, see EnumTypes.py
    #   param is any parameter a particular meggase may be accompanied with
    def ProcessMsg(self, enum, param):
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
            # test the obtained TSF in virtual trading on the given history DPP
            self.TSM.RunModel()
            # once finished, the model will generate TDF list which we need to pass further to SGMM for 
            # analysis
            self.MsgToSGMM(msg.PM_SOTM_READY, self.TDF)
        