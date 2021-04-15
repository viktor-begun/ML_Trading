import SGMM
import CASM
import SOTM

SGMM = TSGMM()
CASM = TCASM()
SOTM = TSOTM()

SGMM.MsgToCASM = CASM.ProcessMsg()
CASM.MsgToSOTM = SOTM.ProcessMsg()