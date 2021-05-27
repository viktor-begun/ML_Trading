from enum import Enum, auto

# Enumerator for the inter-processes mesagging
class FMsg(Enum):
    PM_ECHO = auto()           # simple testing echo back
    PM_NONE = auto()           # none signal
    PM_SOTM_READY = auto()     # SOTM message to SGMM that its analysis cycle completed and results are ready
    PM_CASM_READY = auto()     # CASM message to SOTM that it finished its analysis and result are ready for SOTM to start
    PM_INIT = auto()           # SGMM message to CASM/SOTM to do their inits before runs
    PM_GETLASTERROR = auto()   # SGMM message to CASM/SOTM to get the last detected error
    PM_CLEARERROR = auto()     # SGMM message to CASM/SOTM to clear error message
    PM_CASMSTARTCYCLE = auto() # SGMM message to CASM to start its analysis and write signal into a signal TSF file
    PM_WRITEVAR = auto()       # SGMM message to CASM to write all CASM model variables to the MVF file
    PM_CLOSE = auto()
    PM_VARSTARTIND = auto()    # starting from which index in MVF SOTM/CASM has to read its variables.
    PM_TSF_OBJ = auto()        # message with which the TSF list object is passed
    PM_START = auto()          # message to SGMM to initiate first cycle
    
# Enumerator for the SGMM self-consistent cycles tasks 
class FCycleTask(Enum):
    ctNone = auto()                 # no task
    ctOptimize = auto()             # regular self-consistent cycle
    ctOrdersMap = auto()            # map every tick short and long orders to get full statistics   
    ctVarsMap = auto()              # map, or scan 2 variables to visualize the cost function
    ctValidationTest = auto()       # testing how good models will perform into the future data
    
# Record for keeping all the relevant information about the total energy during the SGMM self-consistent optimization cycle
class FTotalEnergy():
    GlobalMin = 1E10                # lowest achieved energy
    GlobMinIterIndex = 0            # iteration on which best energy was found
    Index = 0                       # last used item index in Hist array
    StuckCnt = 0                    # cycle counter for when energy is not decreasing
    StuckTimeout = 0                # now many cycles with unchanged Etot to wait before shaking variables
    Hist = []                       # history of the total energy variation as a function of cycle index
    flgShakedVars = False           # has to be set true right after variables have been shaked
    

class FVariable():
    Value = 0.0                     # value of the variable
    Type = ""                       # type of the variable, i.e., integer, double, boolean
    Name = ""                       # could be a short description or name
    flgOptimizeable = False         # whether variable can be changed
    ID = 0                          # a unique ID among both CASM and SOTM vars
    LimMin = 0.0
    LimMax = 0.0                    # lower an upper numerical limits it can get
    DefStep = 0.0                   # default step for the variation algorithm
    CurrStep = 0.0                  # current step used for variation
    MinStep = 0.0                   # smallest step allowed step for variation
    MaxStep = 0.0                   # largest step allowed for variation
    Deriv = 0.0                     # Derivative of the error function for this var
    Corr = "CASM"                   # correspondence, either CASM or SOTM
    LastDelta = 0.0                 # last variation of this variable (whether kept or rolled back)
    flgLastSuccess = False          # whether last variation/try lowered total energy
    flgFixedStep = False            # allow to change variation step or use default only
    ShakeStep = 0.0                 # a special value of the step to be used in orded to
                                    # change the current value for overcoming Etot stuck
                                    # FShakeStep is a multiplier to the FCurrStep