# Should have the access to the exchange and should have its own orderbook

# from orderbook import OrderBook
from collections import deque
import numpy as np

class Stock():
    def __init__(self, exchange, price, ticker):
        self.cur_price = price
        self.exchange = exchange
        self.ticker = ticker
        self.bids = {}
        self.offers = {}
        self.past10secs = deque([price])


    def best_bid(self):
        if not self.bids:
            return None
        return max(self.bids.keys())

    def best_offer(self):
        if not self.offers:
            return None
        return min(self.offers.keys())

        

    def add_bid(self, order):
        if order.price == None:
            self.execute_bid(order)
        else:
            while order.price in self.offers and len(self.offers[order.price]) >= 1:
                if self.offers[order.price][0].quantity > order.quantity:
                    self.exchange.execute_match(order, self.offers[order.price][0])
                    break
                else:
                    self.exchange.execute_match(order, self.offers[order.price][0])
                    self.offers[order.price].popleft()

                if len(self.offers[order.price]) == 0:
                    self.offers.pop(order.price)

            if order.quantity > 0:
                if order.price in self.bids:
                    self.bids[order.price].append(order)
                else:
                    self.bids[order.price] = deque([order])
            

    def add_offer(self, order):
        if order.price == None:
            self.execute_offer()
        else:
            while order.price in self.bids and len(self.bids[order.price]) >= 1:
                if self.bids[order.price][0].quantity > order.quantity:
                    self.exchange.execute_match(self.bids[order.price][0], order)
                    break
                else:
                    self.exchange.execute_match(self.bids[order.price][0], order)
                    self.bids[order.price].popleft()
                
                if len(self.bids[order.price]) == 0:
                    self.bids.pop(order.price)

            if order.quantity > 0:
                if order.price in self.offers:
                    self.offers[order.price].append(order)
                else:
                    self.offers[order.price] = deque([order])

    
    # def analyse_last_10(self):
    #     if len(self.past10secs) < 10:
    #         return random.choice(("BID", "OFFER"))
    #     coeffs = np.polyfit(np.linspace(1, 10, 10), self.past10secs, 1)
    #     slope, intercept = coeffs

    #     if slope >= 0:
    #         return "BID"
    #     else:
    #         return "OFFER"

        


    