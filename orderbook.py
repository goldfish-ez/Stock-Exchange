# Should be accessed by the exchange and should have a ticker

class OrderBook():
    def __init__(self, ticker):
        self.ticker = ticker
        