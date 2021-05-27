import SGMM
import CASM
import SOTM
import EnumTypes
import sys
from EnumTypes import FMsg as msg # message that is used to send to class instances from Main.py

# ------------------------ VARIABLES ------------------------ 
 

# create three instances that will work together on the trading model
sgmm = SGMM.TSGMM("SGMMerr.log", "SGMM.log")
if sgmm.FLastError !=  '':
    print(sgmm.FLastError)
    print("Errors detected in SGMM, process stopped")
    sys.exit()
casm = CASM.TCASM("CASMerr.log", "CASM.log")
if casm.FLastError !=  '':
    print(casm.FLastError)
    print("Errors detected in CASM, process stopped")
    sys.exit()
sotm = SOTM.TSOTM("SOTMerr.log", "SOTM.log")
if sotm.FLastError !=  '':
    print(sotm.FLastError)
    print("Errors detected in SOTM, process stopped")
    sys.exit()

# for correct functionality, these three instances need to know the communicating methods
sgmm.MsgToCASM = casm.ProcessMsg
sgmm.MsgToSOTM = sotm.ProcessMsg
casm.MsgToSOTM = sotm.ProcessMsg
sotm.MsgToSGMM = sgmm.ProcessMsg

# initiate start of the first cycle
sgmm.ProcessMsg(msg.PM_START, None)