import SGMM
import CASM
import SOTM
import EnumTypes
import sys

# create three instances that will work together on the trading model
SGMM = TSGMM()
if SGMM.LastError !=  '':
    print(SGMM.LastError)
    print("Errors detected in SGMM, process stopped")
    sys.exit()
CASM = TCASM()
if CASM.LastError !=  '':
    print(CASM.LastError)
    print("Errors detected in CASM, process stopped")
    sys.exit()
SOTM = TSOTM()
if SOTM.LastError !=  '':
    print(SOTM.LastError)
    print("Errors detected in SOTM, process stopped")
    sys.exit()

# for correct functionality, these three instances need to know the communicating methods
SGMM.MsgToCASM = CASM.ProcessMsg()
CASM.MsgToSOTM = SOTM.ProcessMsg()
SOTM.MsgToSGMM = SGMM.ProcessMsg()

# initiate start of the first cycle
SGMM.ProcessMsg(PM_START)