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
        return self.FOrder[-1]

    def __GetOrdersCount(self):
        return len(self.FOrder)
        
    def __AssignUniqueID(self):
        result = self.FIdCnt
        self.FIdCnt = self.FIdCnt + 1

    def __GetOrderIndexByID(self, _id: integer):
        i = integer
        for i in range(0, len(FOrder)-1):
            if self.FOrder[i].FID == _id:
                return = i
        return -1
        
    def __RemoveOrder(self, index: integer):
        tmp = [] # list of TOrderData;
        i = 0
        result = True
        
        if (index<0)or(index>len(FOrder)-1):
            result = false
            self.FLastError = 'Order index is outside of the range'
            return False

        for i in range(0, len(FOrder)-1):
            if i<>index:
                tmp.append(self.FOrder[i])
        
        FOrder.clear()
        for i in range(0, len(tmp)-1):
            self.FOrderappend(tmp[i])
            
        tmp.clear()
        return True

    def __GetLongOrdersCount(self):
        i = 0
        result =  0
        
        for i in range(0, len(FOrder)-1):
            if self.FOrder[i].FType = OrderType.otLong
                result = result + 1
                
        return result

    def __GetShortOrdersCount(self):
        i = 0
        result =  0
        
        for i in range(0, len(FOrder)-1):
            if self.FOrder[i].FType = OrderType.otShort
                result = result + 1
                
        return result
                
    def __GetLastError(self):
  
    # public methods
    def __init__(self, Balance, Spread, Comission, Leverage):
        super().__init__(_FErrorLogFName, _FEventLongName)  # call parent method inherited init first
        self.FIdCnt = 0
        self.FMargin = 0
        self.FBalance = Balance
        self.FLeverage = Leverage
        self.FSpread = Spread
        self.FComission = Comission
        
    def GetOrderByIndex(self, _Index):
        self.FLastError = ''
        if (_Index<0)or(_Index>=len(self.FOrder)):
            self.FLastError = uOrderE3
            return False
            
        return self.FOrder[_index]

    def GetOrder(self, _ID):
        _index = 0
        self.FLastError = ''

        _index = self.GetOrderIndexByID(_ID);
        if _index < 0:
            self.FLastError = uOrderE3
            return False

        return self.FOrder[_index]

    
    def SetOrderTag(self, ID, tag):
        ind = 0

        ind = self.GetOrderIndexByID(ID)
        if (ind<0)or(ind>len(FOrder)-1):
            self.FLastError = 'Cannot find order with the specified ID'
            return False
            
        self.FOrder[ind].FTag = tag
        return True

    def Margin(self):
        i = 0
        result = 0
        
        for i in range(0, len(FOrder)-1):
            result = result + self.FOrder[i].FMargin;
        
        return result
    
    def Equity(self, tick):
        i = 0
        Profit = 0.0
        
        result = self.FBalance
        
        for i in range(0, len(FOrder)-1):
            # the ammount you add to your account by closing this order
            if self.FOrder[i].FType = OrderType.otLong:
                Profit := 100000*self.FOrder[i].FLots*(tick.FClose-self.FOrder[i].FSpread) - 100000*self.FOrder[i].FLots*self.FOrder[i].FOpenPrice;
            elif self.FOrder[i].FType = OrderType.otLong:
                Profit := 100000*self.FOrder[i].FLots*self.FOrder[i].FOpenPrice - 100000*self.FOrder[i].FLots*(tick.FClose+self.FOrder[i].FSpread);
            
        # apply comission
        Profit = Profit - self.FOrder[i].FLots*self.FOrder[i].FComission;

        result = result + Profit
        return result

    # this should be called every tick to analyze all opened orders for SL and TP conditions
    # to be met. The result is the number of orders have been closed
    def OnNewTick(self, tick):
        profit = 0.0
        result := 0;
        i = 0
        
        while i<=len(FOrder)-1:
            if high(FOrder)>=i:
                if self.FOrder[i].FType == OrderType.otLong:
                    # test for stop loss
                    if (i>=0)and(len(FOrder)-1>=i):
                        if tick.FLow<=self.FOrder[i].FStopLoss:
                            CloseOrder(self.FOrder[i].FID, self.Forder[i].FStopLoss);
                            result = result + 1
                            i = -1
                    # test for take profit
                    if (i>=0)and(len(FOrder)-1>=i):
                        if tick.FHigh>=self.FOrder[i].FTakeProfit:
                        CloseOrder(self.FOrder[i].FID, self.Forder[i].FTakeProfit);
                        result = result + 1
                        i = -1
                 
                elif self.FOrder[i].FType == OrderType.otShort:
                    # test for stop loss
                    if (i>=0)and(len(FOrder)-1>=i):
                        if tick.FHigh>=self.FOrder[i].FStopLoss:
                            CloseOrder(self.FOrder[i].FID, self.Forder[i].FStopLoss);
                            result = result + 1
                            i = -1
                 
                    # test for take profit
                    if (i>=0)and(len(FOrder)-1>=i):
                        if tick.FLow<=self.FOrder[i].FTakeProfit:
                            CloseOrder(self.FOrder[i].FID, self.Forder[i].FTakeProfit);
                            result = result + 1
                            i = -1
                i = i + 1
        return result

    # result is positive (order's ID) if seccess, or -1 if errors occured
    # note: _price does not account for spread!
    def OpenOrder(self, _type, _price, _lots, _SL, _TP):
        self.FLastError = ''
        result = -1;

        if _type = OrderType.otEmpty:
            self.FLastError = uOrderE1;
            return
        
        Order = TOrderData()

        Order.FType := _type;
        if _type = OrderType.otLong:
            Order.FOpenPrice := _price + self.FSpread;
            Order.FStopLoss := _price - _SL + self.FSpread;
            Order.FTakeProfit:= _price + _TP + self.FSpread;
        else:
            Order.FOpenPrice := _price - self.FSpread;
            Order.FStopLoss := _price + _SL + self.FSpread;
            Order.FTakeProfit:= _price - _TP + self.FSpread;
            
        Order.FLots := _lots;
        Order.FLeverage := self.FLeverage;
        Order.FSpread := self.FSpread;
        Order.FID := AssignUniqueID;
        Order.FComission := self.FComission;
        Order.FMargin := 100000*_lots*Order.FOpenPrice/self.FLeverage; # the ammount you paid for this order, or, simply Margin

        FOrder.append(Order)

        return Order.FID;
        
    # brutally remove all existing orders
    def ClearOrders():
        self.FOrder = []
        
    def CloseOrder(self, _ID, _price):
        Profit = 0.0
        _index = 0

        self.FLastError = ''

        _index = self.GetOrderIndexByID(_ID);
        if _index<0:
            self.FLastError := uOrderE3;
            return False

        # the ammount you add to your account by closing this order
        if self.FOrder[_index].FType = OrderType.otLong:
            Profit = 100000*self.FOrder[_index].FLots*_price - 100000*self.FOrder[_index].FLots*self.FOrder[_index].FOpenPrice
        elif self.FOrder[_index].FType = OrderType.otShort:
            Profit = 100000*self.FOrder[_index].FLots*self.FOrder[_index].FOpenPrice - 100000*self.FOrder[_index].FLots*_price

        # apply comission
        Profit = Profit - self.FOrder[_index].FLots*self.FOrder[_index].FComission;

        # correct ballance
        self.FBalance = self.FBalance + Profit;

        if callable(OnCloseOrder) == True:
            self.OnCloseOrder(self.FOrder[_index].FID, _price, Profit);

        # remove this order from the orders list
        if not self.RemoveOrder(_index):
            return False

        return True

    def ModifyOrder(self, _ID, _SL, _TP):
        _index = 0
        self.FLastError = ''
        
        _index = self.GetOrderIndexByI(_ID)
        if _index < 0:
            self.FLastError = uOrderE3
            return False
            
        self.FOrder[_index].FStopLoss = _SL
        self.FOrder[_index].FTakeProfit = _TP

