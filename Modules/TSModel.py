# Trading Simulation Model

import TradingAcc

class TTSModel:    
    # ------------------------ VARIABLES ------------------------
    TSF = []        # Trading Signal File
    DPF = []        # Data Pipe File, raw trading history file/list
    TDF = []        # Trading Details File, results of simulated trading
    MVF = []        # Model Variables File, all variables for the current implementation
    
    # Model Variables
    FPip = 0.0              # size of the smallest price variation (broker dependent)
    FSpread = 0.0           # size of the spread in points introduced by the broker, applied to the buy price, i.e. of how much the buy price is higher than the actual stock price
    FSwapShort = 0.0        # daily swap interest rate in annual percentage
    FSwapLong = 0.0         # daily swap interest rate in annual percentage
    FLotSize = 0.0          # how much units is 1 lot
    FLots = 0.0             # number of lots to be traded
    FLevarage = 1           # leverage as 1:FLevarage
    FStopLoss = 1
    FTakeProfit = 1         # stop loss and take profit levels (in point values) to be used
    FBalance 0.0            # amount of money we start with
    FflgRiskBased = True    # use risk level for simulations
    FRiskPercent = 0.0
    FMinLots = 0.0
    FMaxLots = 0.0
    FLotStep = 0.0          # smallest value by which FLots can be changed
    FflgTrailingStop = True
    FComission = 0.0        # round-turn deal per each lot (100k traded)
    FMaxOrderCnt = 1        # maximum number of simultaneously opened orders
    FBolBandPeriod = 1      # Bollinger Band period
    FBBWeightSL = 0.0       # weight factor using BB indicator for Stop Loss
    FBBWeightTP = 0.0       # weight factor using BB indicator for Take Profit
    FReduceSLPerc = 0.0     # max percentage on which SL levels can be reduced in order to accomodate a new order within
    FRiskPercent = 0.0

    
    # ------------------------ METHODS ------------------------ 
    def InitModel(self):
        sett = None  # file variable
        
        # here VarFile.dat to be opened for reading model variables
        try:
            sett = open('VarFile.dat', 'r')
            
            sett.close()
        except:
            return False
        return True
        
    def OnCloseOrder(self, _ID, _closeprice, Profit):
        i = 0.0
    
    def RunModel(self, _DPF, _TSF, _TDF, _MVF):
        self.DPF = _DPF
        self.TSF = _TSF
        self.TDF = _TDF
        self.MVF = _MVF
        
        