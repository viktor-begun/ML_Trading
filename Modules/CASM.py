import EnumTypes
import BaseClass
import MPModel
from EnumTypes import FMsg as msg
import threading
import time

class TCASM(BaseClass.TBaseClass):
    # ------------------------ VARIABLES ------------------------ 
    # upon creation an instance object of TCASM class, its MsgToSOTM variable has to be assigned to TSOTM.ProcessMsg() method
    # this way the TCASM object can send messages to a TSOTM object
    MsgToSOTM = None 
    
    # this is the predictive model (e.g., ARIMA, NN etc.)
    MPM = MPModel.TMPModel()
    
    # other variables
    TSF = []        # Trading Signal File, in this implementation we will use lists, not the memory mapped files
    DPF = []        # Data Pipe File, raw trading history file/list. It is provided by SGMM
    MVF = []        # Model Variables File, all variables for the current implementation (used by MPM)
    VarFName = "CASMVarFile.dat"   # MVF file name
    
    # ------------------------ METHODS ------------------------ 
    # Init any starting state
    def __init__(self, _FErrorLogFName, _FEventLongName):
        super().__init__(_FErrorLogFName, _FEventLongName)  # call parent method inherited init first
        # read all settings for this optimization
        if not self.LoadSettings():
            self.LogError("Error while loading settings")    
        # read all variable provided in the VarFName file required for MPM
        if not self.LoadVariables():
            self.LogError("Error during loading variables. Check if " + str(self.VarFName) + " exists")
        # init model that is used to predict market move (ARIMA etc.)
        if not self.MPM.InitModel():
            self.LogError("Failed to initialize Marker Prediction Model")
        # start self.Poll as a thread, it will be periodically checking for any pending messagges to serve
        thread = threading.Thread(target=self.Poll, args=())
        thread.daemon = True                            
        thread.start() 
    
    # Load settings
    def LoadSettings(self):
        sett = None    # settings file variable
        
        # here settCASM.ini to be opened and parameter to be read
        try:
            sett = open('settCASM.ini')
            
            
            sett.close()
        except:
            return False
        return True
        
    # Load variables
    def LoadVariables(self):
        FVar = None    # settings file variable
        
        # here VarFName to be opened and parameter to be read
        try:
            self.FVar = open(self.VarFName)
            set1 = self.FVar.readline()
            set2 = self.FVar.readline()
            set3 = self.FVar.readline()
        except:
            return False
        return True        
    
    def Poll(self):
        # this will be polling the RecMsg variable that contains an unprocessed message
        while True:
            if self.RecMsg == msg.PM_CASMSTARTCYCLE:
                # MPR - Market Prediction Results, the results of the MPModel to be written in this list by MPM.RunModel
                MPR = []
                # here the MPM should be called which will generate expectations on the market moving direction
                # for every data point (except truncated start) using current implementation (ARIMA, MA, 
                # Bollinger Bands, LSTM, etc.)
                self.MPM.RunModel(self.DPF, MPR, self.MVF)
                # after market move expectations have been generated, the trading signals (TSF) should be generated next
                self.GenerateSignals(MPR)
                self.Log(0, 'CASM finished')
                # after trading signals (buy/sell/do nothing) have been generated, a message to SOTM object should be sent
                self.MsgToSOTM(msg.PM_CASM_READY, self.TSF, self.DPF, self.MVF)
                self.RecMsg = None
            else:
                time.sleep(0.01)
            
            
    # The base functionality class declares the message-type interaction between the instances of different classes
    # The parent class shall implement its way of processing of the received messages
    #   enum parameter is the Message it has received, see EnumTypes.py
    #   param is any parameter a particular meggase may be accompanied with
    def ProcessMsg(self, enum, param, param2):
        # initialize
        if  enum == msg.PM_INIT:
            # Market Prediction Results, the MPM model will write to this list the results of its analysis
            # this list is temporary and it can be kept local to this routine
            MPR = []
            # do init. Note: in python __init__ is automatically called upon creating a class instance.
            # just in case we need to re-init, keep  this message
            self.__init__(self, "CASMerr.log", "CASM.log")
         
        # return last error
        elif enum == msg.PM_GETLASTERROR:
            return self.FLastError
            
        # SGMM asked to start a new cycle of signal generation
        elif enum == msg.PM_CASMSTARTCYCLE:
            # for this message the param is pointing to a DPF data pipe file, i.e., raw price historic chart
            self.DPF = param
            # update Model Variables File
            self.MVF = param2
            # to avoid recursion just record the message we received and return. The rest will be handled by self.Poll()
            self.RecMsg = enum
        
    
    # Here, the trading signal for the given history will be generated and writtent to a TSF and SOTM object
    # will be informed by messaging to it
    def GenerateSignals(self, MPR):
        self.TSF = [0.0] * len(MPR)
        for i in range(0, len(MPR)-1):
            self.TSF[i] = 0.0 # just a dummy cycle for now