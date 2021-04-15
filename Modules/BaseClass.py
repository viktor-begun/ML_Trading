import EnumTypes

#==================================================================================================================
#   This is the base class which defines basic functionality for all SGMM, CASM, and SOTM classes
#==================================================================================================================

class TBaseClass(object):
    FErrorLogFName = '' # File name for the error log
    FEventLogName = ''  # File name for events logging
    FLastError = ''     # Description of the last error occured

    # Init any starting state
    def __init__(self, _FErrorLogFName, _FEventLongName):
        FErrorLogFName = _FErrorLogFName
        FEventLogName = _FEventLongName
       
    # The base functionality class declares the message-type interaction between the instances of different classes
    # The parent class shall implement its way of processing of the received messages
    def ProcessMsg(self, enum, param)
    
    # For error logging purposes
    def LogError(self, _ErrorText):
    
    # For events logging purposes, level 0 - most important info, leve 1 - debug info
    def Log(self, _LogLevel, _LogText):