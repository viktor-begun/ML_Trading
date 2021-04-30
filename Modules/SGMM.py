import EnumTypes
import BaseClass

class TSGMM(TBaseClass):
    # upon creation an instance object of TSGMM class, its MsgToCASM variable has to be assigned to TCASM.ProcessMsg() method
    # this way the TSGMM object can send messages to a TCASM object
    MsgToCASM = None 
    ETot = FTotalEnergy         # structure for total energy being minimized
    CycleCount = 0              # counter of the completed optimization iterations
    FSett = None                # settings file variable
    
    # This will load all settings required for the calculations from a disk data file ('settSGMM.ini')
    def LoadSettings(self):
        # here settSGMM.ini to be opened and parameter to be read
        try:
            self.FSett = open('settSGMM.ini')
            set1 = self.FSett.readline()
            set2 = self.FSett.readline()
            set3 = self.FSett.readline()
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
            self.Etot.Hist.append([0.0, 0])   # array of the fixed large size to avoid exc essive memory expansion in runtime
        self.Etot.StuckCnt = 0;
        self.Etot.GlobalMin = 1e9;
        
        # 2 - LOAD ALL SETTING FOR THE CALCULATIONS
        if not self.LoadSettings():
            LogError('Error while loading settings. Check if file settSGMM.ini exists')
        
        # 3 - CHECK WHETHER ALL REQUIRED FILES EXIST
        
        # 4 - CREATE MEMORY MAPPED DATA PIPE FILES
        
        # 6 - CREATE MEMORY MAPPED INTER_PROCESS TEXT MESSAGES EXCHANGE
        
        # 7 - CREATE MEMORY MAPPED TRADING SIGNAL FILES
        
        # 8 - CREATE MEMORY MAPPED MODEL VARIABLES FILE
        
        # 9 - CREATE MEMORY MAPPED TRADES DETAILS FILE
        
        # 11 - CREATE MEMORY MAPPED ADVANCED ACCOUNT DETAILS FILE
        
        # 12 - POPULATE DPF WITH DATA FROM THE DISK
        
        # 13 - IF PREDICTABILITY TESTS WILL BE USED, PREPARE DATA FOR ITS USAGE
        
        # 14 - RUN AS MANY CASM.EXE INSTANCES AS MANY DATA PIPES WE HAVE
        
        # 15 - RUN AS MANY SOTM.EXE INSTANCES AS MANY DATA PIPES WE HAVE
        
        # 16 - ONCE ALL SOTM ARE RUNNING, SEND THEIR HWND TO THEIR CASM PARTNERS
        
        # 17 - UPDATE ALL SOTM WITH THE SGMM HANDLE
        
        # 18 - ASK ALL CASM TO GET ACCESS TO THE MODEL VARIABLES FILE (MVF)
        
        # 19 - ASK CASM0 TO POPULATE MVF WITH OWN VARIABLES (SAME AMONG ALL CASM INSTANCES)
        
        # 20 - SEND TO ALL CASM INSTANCES THEIR STARTING INDEX FOR VARIABLES IN MVF FILE
        
        # 22 - ASK SOTM0 TO POPULATE (APPENDING) MVF WITH OWN VARIABLES (SAME AMONG ALL SOTM INSTANCES)
        
        # 23 - BUILD A LIST OF INDICES (IN VARFILE) OF OPTIMIZEABLE VARIABLES
        
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
        if  enum = PM_ECHO:
            print('Echo back')
        # restarting cycle once SOTM finished
        elif enum = PM_SOTM_READY:
            # once SOTM finished simulation of the trading, analyze the results, decide whether to keep the
            # variables or to roll them back and apply new variations
            self.AnalyzeCycle()
            # when cyccle was completed and variables have been varied, start next cycle by messaging to CASM
            self.MsgToCASM(PM_CASMSTARTCYCLE)
        # starting the first cycle of calculations
        elif enum = PM_CASMSTARTCYCLE:
            