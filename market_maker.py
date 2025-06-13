from trader import Trader

class MarketMaker(Trader):
    def calculate_price(self, ticker, time):
        cur_price = self.exchange.get_cur_price(ticker)
        best_bid = self.exchange.get_best_bid(ticker)
        best_sell = self.exchange.get_best_offer(ticker)
        if best_bid == None:
            best_bid = cur_price
        if best_sell == None:
            best_sell = cur_price
        price = float(best_sell + best_bid) / 2 
        return price
        
    def place_order(self, quantity, ticker, time):
        price = self.calculate_price(ticker, time)
        self.place_limit_order(type= "BID", quantity=quantity, ticker=ticker, time=time, price=price-0.2)
        self.place_limit_order(type= "OFFER", quantity=quantity, ticker=ticker, time=time, price=price+0.2)
    