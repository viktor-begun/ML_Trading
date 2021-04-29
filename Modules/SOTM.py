import EnumTypes
import BaseClass
import TSModel

class TSOTM(TBaseClass):
    # ------------------------ VARIABLES ------------------------ 
    # upon creation an instance object of TSOTM class, its MsgToSGMM variable has to be assigned to SGMM.ProcessMsg() method
    # this way the TSOTM object can send messages to a TSGMM object
    MsgToSGMM = None
    
    # this is the trading simulation model
    TSM = TTSModel()
    
    # Trading Signal File, in this implementation we will use lists, not the memory mapped files
    # CASM will be building this list and sending to SOTM for analysis
    TSF = []
    
    # ------------------------ METHODS ------------------------ 
    # Load settings
    def LoadSettings(self):
       # here settSOTM.ini to be opened and parameter to be read
        try:
            self.FSett = open('settSOTM.ini')
            set1 = self.FSett.readline()
            set2 = self.FSett.readline()
            set3 = self.FSett.readline()
        except:
            resturn False
        return True
        
    # Init any starting state
    def __init__(self, _FErrorLogFName):
        super().__init__()  # call parent method inherited init first
        self.FErrorLogFName = _FErrorLogFName
        # read all settings for this optimization
        if not self.LoadSettings:
            self.LogError("Error while loading settings")
            
    # The base functionality class declares the message-type interaction between the instances of different classes
    # The parent class shall implement its way of processing of the received messages
    #   enum parameter is the Message it has received, see EnumTypes.py
    #   param is any parameter a particular meggase may be accompanied with
    def ProcessMsg(self, enum, param):
        if  enum = PM_INIT:
            # do init
            __init__(self, "SOTMerr.log")
        elif enum = PM_CASM_READY:
            # by now, CASM should have finished writting into TSF and we ready to simulate trading
            # on the given history DPF