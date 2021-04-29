# Trading Simulation Model

class TTSModel:    
    # ------------------------ VARIABLES ------------------------
    VarFile = None # file containing variables for the model
    
    def InitModel(self):
        # here VarFile.dat to be opened for reading model variables
        try:
            self.VarFile = open('VarFile.dat', 'r')
            # skip comments
            for i in range(0,3):
                self.VarFile.readline()
            # read variables
            set1 = self.VarFile.readline()
            set2 = self.VarFile.readline()
            set3 = self.VarFile.readline()
        except:
            return False
        return True
    
    def RunModel(self):