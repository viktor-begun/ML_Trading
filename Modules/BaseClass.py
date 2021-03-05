import EnumTypes

#==================================================================================================================
#   This is the base class which defines basic functionality for all SGMM, CASM, and SOTM classes
#==================================================================================================================

class TBaseClass(object):
    FErrorLogFName = '' # File name for the error log
    FLastError = ''     # Description of the last error occured

    # Init any starting state
    def __init__(self, _FErrorLogFName):        
       
    # The base functionality class declares the message-type interaction between the instances of different classes
    def Send(self, enum, param)
    
    # For error logging purposes
    def LogError(self, ErrorText):
    
    # For events logging purposes, level 0 - most important info, leve 1 - debug info
    def Log(self, LogLevel, LogText):