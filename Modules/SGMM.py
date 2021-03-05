import EnumTypes
import BaseClass

class TSGMM(TBaseClass):
    # upon creation an instance object of SGMM class, its MsgCASM has to be assigned to CASM.Send() method
    # this way the SGMM object can communicate with CASM object
    MsgCASM = None 
    ETot = FTotalEnergy         # structure for total energy being minimized
    CycleCount = 0              # counter of the completed optimization iterations
    
    # This will load all settings required for the calculations from a disk data file ('settSGMM.ini')
    def LoadSettings(self):
    
    # Prepare the simulations
    def __init__(self):
        super().__init__()  # call parent method inherited init first
        
        # 1 - INIT BASIC VARIABLES
        self.Log(0, 'SGMM cycle started');
        CycleCount = 0
        for i in range(0,99999):    # not an elegant way, but doing this I can get a fixed size of the Etot.Hist
            Etot.Hist.append([0.0, 0])   # array of the fixed large size to avoid exc essive memory expansion in runtime
        Etot.StuckCnt = 0;
        Etot.GlobalMin = 1e9;
        
        # 2 - LOAD ALL SETTING FOR THE CALCULATIONS
        self.LoadSettings()
        
        # 3 - CHECK WHETHER ALL REQUIRED FILES EXIST
