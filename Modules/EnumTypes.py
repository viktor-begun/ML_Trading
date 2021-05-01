from enum import Enum, auto

# Enumerator for the inter-processes mesagging
class Msg(Enum):
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
class CycleTask(Enum):
    ctNone = auto()                 # no task
    ctOptimize = auto()             # regular self-consistent cycle
    ctOrdersMap = auto()            # map every tick short and long orders to get full statistics   
    ctVarsMap = auto()              # map, or scan 2 variables to visualize the cost function
    ctValidationTest = auto()       # testing how good models will perform into the future data
    
# Record for keeping all the relevant information about the total energy during the SGMM self-consistent optimization cycle
class TotalEnergy():
    GlobalMin = 1E10                # lowest achieved energy
    GlobMinIterIndex = 0            # iteration on which best energy was found
    Index = 0                       # last used item index in Hist array
    StuckCnt = 0                    # cycle counter for when energy is not decreasing
    StuckTimeout = 0                # now many cycles with unchanged Etot to wait before shaking variables
    Hist = []                       # history of the total energy variation as a function of cycle index
    flgShakedVars = false           # has to be set true right after variables have been shaked
    

    