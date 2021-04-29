import SGMM
import CASM
import SOTM

# create three instances that will work together on the trading model
SGMM = TSGMM()
CASM = TCASM()
SOTM = TSOTM()

# for correct functionality, these three instances need to know the communicating methods
SGMM.MsgToCASM = CASM.ProcessMsg()
CASM.MsgToSOTM = SOTM.ProcessMsg()
SOTM.MsgToSGMM = SGMM.ProcessMsg()

# for now, several inits that have to be done after all object have been created
# it can be moved into automatic after-init by instances themself, but for now it is fine
SOTM.TSF = CASM.TSF