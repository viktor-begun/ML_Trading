# Trading Simulation Model

class TTSModel:    
    # ------------------------ VARIABLES ------------------------
    
    def InitModel(self):
        sett = None  # file variable
        
        # here VarFile.dat to be opened for reading model variables
        try:
            sett = open('VarFile.dat', 'r')
            
            sett.close()
        except:
            return False
        return True
    
    def RunModel(self):
        i = 0.0