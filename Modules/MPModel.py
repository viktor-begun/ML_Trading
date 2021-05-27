# Market Prediction Model


class TMPModel:
    # ------------------------ VARIABLES ------------------------
    
    def InitModel(self):
        FSett = None    # settings file variable
    
        # here VarFile.dat to be opened for reading model variables
        try:
            FSett = open('CASMVarFile.dat', 'r')
            
            FSett.close()
        except:
            return False
        return True
    
    # this is the core of this class. 
    # DPR is a pointer to a list
    # MPR is a pointer to a list
    # in DPR every line is one history data point/tick
    #   every line in DPR is stored in text ["Local time" "Open" "High" "Low" "Close" "Volume"]
    #   data type for enties represents is  [datetime double double double double double]
    # in MPR every line is one history data point/tick
    #   every line in MPR is stored in text ["param1" "param2" ... "paramN"]
    #   date types and the number of entries  will vary depending on the current implementation
    # RunModel takes the market historical price chart in DPF and then does
    # the analysis using cuurent implementation (ARIMA, BB, LSTM, etc.) to provide a number of values 
    # characterising each historical tick of data (e.g., predictions, expectations, sentiments, etc.)
    def RunModel(self, DPF, MPR, MVF):
        i = 0.0 # add here simple moving average implementation