import EnumTypes
import BaseClass
import MPModel

class TCASM(TBaseClass):
    # ------------------------ VARIABLES ------------------------ 
    # upon creation an instance object of TCASM class, its MsgToSOTM variable has to be assigned to TSOTM.ProcessMsg() method
    # this way the TCASM object can send messages to a TSOTM object
    MsgToSOTM = None 
    
    # this is the predictive model (e.g., ARIMA, NN etc.)
    MPM = TMPModel()
    
    # other variables
    FSett = None    # settings file variable
    TSF = []        # Trading Signal File, in this implementation we will use lists, not the memory mapped files
    DPF = []        # Data Pipe File, raw trading history file/list. It is provided by SGMM
    
    # ------------------------ METHODS ------------------------ 
    # Load settings
    def LoadSettings(self):
        # here settCASM.ini to be opened and parameter to be read
        try:
            self.FSett = open('settCASM.ini')
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
        if not LoadSettings():
            self.LogError("Error while loading settings")    
        # init model that is used to predict market move (ARIMA etc.)
        if not self.MPM.InitModel():
            self.LogError("Failed to initialize Marker Prediction Model, check if VarFile.dat exists")
        # TSF is a python list, send it to SOTM
        
        
    
    # The base functionality class declares the message-type interaction between the instances of different classes
    # The parent class shall implement its way of processing of the received messages
    #   enum parameter is the Message it has received, see EnumTypes.py
    #   param is any parameter a particular meggase may be accompanied with
    def ProcessMsg(self, enum, param):
        if  enum = PM_INIT:
            # Market Prediction Results, the MPM model will write to thil list the results of its analysis
            # this list is temporary and it can be kept local to this routine
            MPR = []
            # do init. Note: in python __init__ is automatically called upon creating a class instance.
            # just in case we need to re-init, keep  this message
            self.__init__(self, "CASMerr.log")
        elif enum = PM_CASMSTARTCYCLE:
            # for this message the param is pointing to a DPF data pipe file, i.e., raw price historic chart
            self.DPF = param
            # here the MPM should be called which will generate expectations on the market moving direction
            # for every data point (except truncated start) using current implementation (ARIMA, MA, 
            # Bollinger Bands, LSTM, etc.)
            self.MPM.RunModel(self.DPF, MPR)
            # after market move expectations have been generated, the trading signals should be generated next
            self.GenerateSignals(MPR, self.TSF)
            # after trading signals (buy/sell/do nothing) have been generated, a message to SOTM object should be sent
            self.MsgToSOTM(PM_CASM_READY, self.TSF)
        elif enum = 
    
    # Here, the trading signal for the given history will be generated and writtent to a TSF and SOTM object
    # will be informed by messaging to it
    def GenerateSignals(self)