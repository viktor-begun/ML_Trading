import BaseClass
import EnumTypes

uOrderE1 = 'Cannot add an empty type order';
uOrderE3 = 'Cannot find an open order with the ID provided';

class TOrderType(Enum):
    otEmpty = Auto()
    otLong = Auto()
    otShort = Auto()

OrderType = TOrderType()

class TOrderData():
    FID = 1             # unique ID of the order
    FType = Enum        # long or short, osEmpty is undefined here
    FOpenPrice = 0.0    # price at which is has been opened, spread is accounted, i.e. the final price one paid to place an order
    FLots = 0.0         # amount of lots traded. 1 lot = 100k
    FLeverage = 1
    FStopLoss = 0.0
    FTakeProfit = 0.0
    FSpread = 0.0
    FTag = 1            # for storing extra info
    FComission = 0.0    # round-turn deal per each lot (100k traded)
    FMargin = 0.0       # price paid to open this order


class TTradingAccount(BaseClass.TBaseClass):
    
    # ------------------------ VARIABLES ------------------------
    OnCloseOrder = None
    FIdCnt = 1 # counter for assigning ID's to the orders
    FLastError = ''
    FOrder = []
    FBalance = 0.0 # account balance
    FLeverage = 1 # 1:xxx leverage of the trading account
    FSpread = 0.0 # spread in absolute value, so far fixed only
    FMargin = 0.0 # amount you paid to open all currently open orders
    FComission = 0.0 # commission on the round-turn order

    # ------------------------ PROPERTIES ------------------------
    OrderCount = property(GetOrdersCount)
    ShortCount = property(GetShortOrdersCount)
    LongCount = property(GetLongOrdersCount)
    Last = property(GetLastOrder)
    LastError = property(GetLastError)

    # ------------------------ METHODS ------------------------
    # private methods defined by double underscore __
    def __GetLastOrder(self): 
    def __GetOrdersCount(self):
    def __AssignUniqueID(self):
    def __GetOrderIndexByID(self, _id: integer):
    def __RemoveOrder(self, index: integer):
    def __GetLongOrdersCount(self):
    def __GetShortOrdersCount(self):
    def __GetLastError(self):
  
    # public methods
    def __init__(self, Balance, Spread, Comission, Leverage):
        super().__init__(_FErrorLogFName, _FEventLongName)  # call parent method inherited init first
        
    def GetOrderByIndex(self, _Index):
    def GetOrder(self, _ID):
    
    def ClearOrders: # brutally remove all existing orders
    def SetOrderTag(self, ID, tag):
    def Margin(self):
    def Equity(self, tick):

    # this should be called every tick to analyze all opened orders for SL and TP conditions
    # to be met. The result is the number of orders have been closed
    def OnNewTick(self, tick):

    # result is positive (order's ID) if seccess, or -1 if errors occured
    # note: _price does not account for spread!
    def OpenOrder(self, _type, _price, _lots, _SL, _TP):
        self.FLastError = ''
        result = -1;

        if _type = otEmpty:
            self.FLastError = uOrderE1;
            return
        
        Order = TOrderData()

        Order.FType := _type;
        if _type = OrderType.otLong:
            Order.FOpenPrice := _price + FSpread;
            Order.FStopLoss := _price - _SL + FSpread;
            Order.FTakeProfit:= _price + _TP + FSpread;
        else:
            Order.FOpenPrice := _price - FSpread;
            Order.FStopLoss := _price + _SL + FSpread;
            Order.FTakeProfit:= _price - _TP + FSpread;
        end;
        FOrder[high(FOrder)].FLots := _lots;
        FOrder[high(FOrder)].FLeverage := FLeverage;
        FOrder[high(FOrder)].FSpread := FSpread;
        FOrder[high(FOrder)].FID := AssignUniqueID;
        FOrder[high(FOrder)].FComission := FComission;
        FOrder[high(FOrder)].FMargin := 100000*_lots*FOrder[high(FOrder)].FOpenPrice/FLeverage; # the ammount you paid for this order, or, simply Margin

        return FOrder[high(FOrder)].FID;


    # true if no errors, false if errors occured
    # note: _price does not account for spread! Spread is used from TOrderData updated in OpenOrder
    def CloseOrder(self, _ID, _price):
    def ModifyOrder(self, _ID, _SL, _TP):
