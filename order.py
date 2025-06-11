# Should have the access to the stock and the trader id of the person placing the order

class Order:
    def __init__(self, ticker, type, quantity, price, trader_id, time):
        self.price = price
        self.quantity = quantity
        self.type = type
        self.ticker = ticker
        self.trader_id = trader_id
        self.time = time


class BuyOrder(Order):
    def __init__(self, ticker, type, quantity, price, trader_id, time):
        super().__init__(ticker, type, quantity, price, trader_id, time)


class SellOrder(Order):
    def __init__(self, ticker, type, quantity, price, trader_id, time, shares):
        super().__init__(ticker, type, quantity, price, trader_id, time)
        self.shares = shares
        