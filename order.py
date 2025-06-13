# Should have the access to the stock and the trader id of the person placing the order

class Order:
    def __init__(self, ticker, type, quantity, price, trader_id, time):
        self.price = price
        self.quantity = quantity
        self.type = type
        self.ticker = ticker
        self.trader_id = trader_id
        self.time = time

    def __lt__(self, other):
        pass


class BuyOrder(Order):
    def __init__(self, ticker, type, quantity, price, trader_id, time):
        super().__init__(ticker, type, quantity, price, trader_id, time)

    def __lt__(self, other):
        self_price_priority = -self.price
        other_price_priority = -other.price
        
        if self_price_priority != other_price_priority:
            return self_price_priority < other_price_priority
        else:
            return self.time< other.time

        


class SellOrder(Order):
    def __init__(self, ticker, type, quantity, price, trader_id, time, shares):
        super().__init__(ticker, type, quantity, price, trader_id, time)
        self.shares = shares
    
    def __lt__(self, other):
        self_price_priority = self.price
        other_price_priority = other.price
        
        if self_price_priority != other_price_priority:
            return self_price_priority < other_price_priority
        else:
            return self.time< other.time
        