import SGMM
import CASM
import SOTM
import EnumTypes

# create three instances that will work together on the trading model
SGMM = TSGMM()
CASM = TCASM()
SOTM = TSOTM()

# for correct functionality, these three instances need to know the communicating methods
SGMM.MsgToCASM = CASM.ProcessMsg()
CASM.MsgToSOTM = SOTM.ProcessMsg()
SOTM.MsgToSGMM = SGMM.ProcessMsg()

# initiate start of the first cycle
SGMM.ProcessMsg(PM_START)