import EnumTypes
import BaseClass
from datetime import datetime

#==================================================================================================================
#   This is the base class which defines basic functionality for all SGMM, CASM, and SOTM classes
#==================================================================================================================

class TBaseClass(object):
    FErrorLogFName = '' # File name for the error log
    FEventLogName = ''  # File name for events logging
    FLastError = ''     # Description of the last error occured
    FLogLevel = 0       # logging level, 0 is basic info, 1 is debugging
    RecMsg = None       # Any message that has been received from another class instance and to be processed
    
    
    # Init any starting state
    def __init__(self, _FErrorLogFName, _FEventLongName):
        self.FErrorLogFName = _FErrorLogFName
        self.FEventLogName = _FEventLongName
       
    # The base functionality class declares the message-type interaction between the instances of different classes
    # The parent class shall implement its way of processing of the received messages
    def ProcessMsg(self, enum, param):
        i = 1.0
        
    # For error logging purposes
    def LogError(self, _ErrorText):
        self.FLastError = _ErrorText
        f = open(self.FErrorLogFName, 'a') 
        dt = datetime.now()
        dtt = dt.strftime("%d/%m/%Y %H:%M:%S")
        f.write(dtt+'\t'+_ErrorText+'\n')
        f.close
        
    # For events logging purposes, level 0 - most important info, level 1 - full debug info
    def Log(self, _Level, _LogText):
        # do not log everything if the self.LogLevel is setup for basic logging
        if _Level == 1 and self.LogLevel == 0: return
        
        f = open(self.FEventLogName, 'a') 
        dt = datetime.now()
        dtt = dt.strftime("%d/%m/%Y %H:%M:%S")
        f.write(dtt+'\t'+_LogText+'\n')
        f.close