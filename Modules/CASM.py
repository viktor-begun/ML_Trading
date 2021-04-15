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
    
    # ------------------------ METHODS ------------------------ 
    # Load settings
    def LoadSettings(self):
        # here settCASM.ini to be opened and parameter to be read
        return True;
    
    # Init any starting state
    def __init__(self, _FErrorLogFName):
        super().__init__()  # call parent method inherited init first
        FErrorLogFName = _FErrorLogFName
        # read all settings for this optimization
        if not LoadSettings:
            LogError("Error while loading settings")    
        # init model that is used to predict market move (ARIMA etc.)
        MPM.InitModel()        
    
    # The base functionality class declares the message-type interaction between the instances of different classes
    # The parent class shall implement its way of processing of the received messages
    #   enum parameter is the Message it has received, see EnumTypes.py
    #   param is any parameter a particular meggase may be accompanied with
    def ProcessMsg(self, enum, param):
        if  enum = PM_INIT:
            # do init
            __init__(self, "CASMerr.log")
        elif enum = PM_CASMSTARTCYCLE:
            # here the PM should be called which will generate expectations on the market moving direction
            # for every data point (except truncated start) using current implementation (ARIMA, MA, 
            # Bollinger Bands, LSTM, etc.)
            MPM.RunModel()
            # after market move expectations have been generated, the trading signals should be generated next
            GenerateSignals()
            # after trading sygnals (buy/sell/do nothing) have been generated, a message to SOTM object should be sent
            MsgToSOTM(PM_CASM_READY)
        elif enum = 
    
    # Here, the trading signal for the given history will be generated and writtent to a TSF and SOTM object
    # will be informed by messaging to it
    def GenerateSignals(self)