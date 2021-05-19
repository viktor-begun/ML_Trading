# Note on variables definitions.    All variables that are important to keep track are defined explicitly and globally.
#                                   All variables that are just used one time are defined righe when needed within methods

import EnumTypes
import BaseClass
import os.path
from os import path

class TSGMM(TBaseClass):
    # upon creation an instance object of TSGMM class, its MsgToCASM variable has to be assigned to TCASM.ProcessMsg() method
    # this way the TSGMM object can send messages to a TCASM object
    MsgToCASM = None 
    ETot = FTotalEnergy         # structure for total energy being minimized
    CycleCount = 0              # counter of the completed optimization iterations
    TDF = []                    # Trades Details File, result of virtual trading generated by SOTM
    DPF = []                    # Data Pipe File, raw trading history price chart
    HistFName = ''              # File Name of the training history DPF
    ModelVarFName = ''          # file name where variables giving best performance will be stored 
    
    # This will load all settings required for the calculations from a disk data file ('settSGMM.ini')
    def LoadSettings(self):
        str = ''
        sett = None  # file variable
        # here settSGMM.ini to be opened and parameter to be read
        try:
            if not path.exists('settSGMM.ini'):
                self.LogError('File settSGMM.ini does not exist')
                return False
                
            FSett = open('settSGMM.ini')
                
            FSett.readline() # [LogLevel]
            str = FSett.readline() # value
            self.FLogLevel = int(str)
            
            FSett.readline() # [DataPipeFName] <- input file
            str = FSett.readline() # value
            self.HistFName = str
            
            # [flgLogTradeHist]
            # [LogEtotFName] <- output file
            # [LogOrdersDetailsFName] <- output file
            # [ModelVarFName] <- output file
        except:
            resturn False
        return True
        
    # Prepare the simulations
    def __init__(self):
        super().__init__()  # call parent method inherited init first
        
        # 1 - INIT BASIC VARIABLES
        self.Log(0, 'SGMM cycle started');
        self.CycleCount = 0
        for i in range(0,99999):    # not an elegant way, but doing this I can get a fixed size of the Etot.Hist
            self.Etot.Hist.append([0.0, 0])   # array of the fixed large size to avoid excessive memory expansion in runtime
        self.Etot.StuckCnt = 0;
        self.Etot.GlobalMin = 1e9;
        
        # 2 - LOAD ALL SETTING FOR THE CALCULATIONS
        if not self.LoadSettings():
            self.LogError('Error while loading settings')
            
        # 3 - CHECK WHETHER ALL REQUIRED FILES EXIST
        if not path.exists(self.HistFName):
            self.LogError("The specified history file "+self.HistFName+" does not exist")
            
        
        # - 4 - CREATE MEMORY MAPPED DATA PIPE FILES
        
        # - 6 - CREATE MEMORY MAPPED INTER_PROCESS TEXT MESSAGES EXCHANGE
        
        # - 7 - CREATE MEMORY MAPPED TRADING SIGNAL FILES
        
        # - 8 - CREATE MEMORY MAPPED MODEL VARIABLES FILE
        
        # - 9 - CREATE MEMORY MAPPED TRADES DETAILS FILE
        
        # - 11 - CREATE MEMORY MAPPED ADVANCED ACCOUNT DETAILS FILE
        
        # 12 - POPULATE DPF WITH DATA FROM THE DISK
        hfile = open(self.HistFName, "r")
        count = 0
        for line in hfile:
            count += 1
            sline = line.strip()
            if count != 1:   # 1st line in our history files is column names, don't include in data
            self.DPF.append(sline.split(','))
        hfile.close()
        
        # 13 - IF PREDICTABILITY TESTS WILL BE USED, PREPARE DATA FOR ITS USAGE
        
        # - 14 - RUN AS MANY CASM.EXE INSTANCES AS MANY DATA PIPES WE HAVE
        
        # - 15 - RUN AS MANY SOTM.EXE INSTANCES AS MANY DATA PIPES WE HAVE
        
        # - 16 - ONCE ALL SOTM ARE RUNNING, SEND THEIR HWND TO THEIR CASM PARTNERS
        
        # - 17 - UPDATE ALL SOTM WITH THE SGMM HANDLE
        
        # - 18 - ASK ALL CASM TO GET ACCESS TO THE MODEL VARIABLES FILE (MVF)
        
        # 19 - ASK CASM0 TO POPULATE MVF WITH OWN VARIABLES (SAME AMONG ALL CASM INSTANCES)
        
        # - 20 - SEND TO ALL CASM INSTANCES THEIR STARTING INDEX FOR VARIABLES IN MVF FILE
        
        # 22 - ASK SOTM0 TO POPULATE (APPENDING) MVF WITH OWN VARIABLES (SAME AMONG ALL SOTM INSTANCES)
        
        # - 23 - BUILD A LIST OF INDICES (IN VARFILE) OF OPTIMIZEABLE VARIABLES
        
        # 24 - DO ANY OTHER REQUESTED TASK AS CONFIGURED
        
        # 25 - INITIATE FIRST SELF-CONSISTENT CYCLE
        
    def AnalyzeCycle(self):
        # here the profit curves from SOTM (TDF file) is analyzed and variables are varied/adjusted
    
    # The base functionality class declares the message-type interaction between the instances of different classes
    # The parent class shall implement its way of processing received messages
    #   enum parameter is the Message it has received, see EnumTypes.py
    #   param is any parameter a particular meggase may be accompanied with
    def ProcessMsg(self, enum, param):
        # echo message for debugging
        if enum = PM_ECHO:
            print('Echo back')
        # restarting cycle once SOTM finished
        elif enum = PM_SOTM_READY:
            # once SOTM finished simulation of the trading, analyze the results, decide whether to keep the
            # variables or to roll them back and apply new variations
            self.TDF = param # param for this message will point to the TDF list generated by SOTM
            self.AnalyzeCycle()
            # when cycle was completed and variables have been varied, start next cycle by messaging to CASM
            self.MsgToCASM(PM_CASMSTARTCYCLE, self.DPF)
        # starting the first cycle of calculations
        elif enum = PM_START:
            self.MsgToCASM(PM_CASMSTARTCYCLE, self.DPF)
            