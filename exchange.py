# Should act as a bridge between the traders and the stocks

from order import BuyOrder, SellOrder

class Exchange:
    def __init__(self):
        self.stocks = {}
        self.traders = {}

    def place_bid(self, trader, quantity, ticker, time, price):
        order = BuyOrder(ticker, "BID", quantity, price, trader.id, time)
        self.stocks[ticker].add_bid(order)

    def place_offer(self, trader, quantity, ticker, time, price, shares):
        order = SellOrder(ticker, "OFFER", quantity, price, trader.id, time, shares)
        self.stocks[ticker].add_offer(order)

    def execute_match(self, buy_order, sell_order):
        if buy_order.quantity >= sell_order.quantity:
            q = sell_order.quantity
        else:
            q = buy_order.quantity
        buy_order.quantity -= q
        sell_order.quantity -= q
        shares = sell_order.shares

        buyer = self.traders[buy_order.trader_id]
        seller = self.traders[sell_order.trader_id]

        buyer.deduct_money(q * buy_order.price)
        buyer.buy_share(shares, sell_order.ticker)

        seller.receive_money(q * buy_order.price)

        self.stocks[sell_order.ticker].cur_price = buy_order.price
        self.stocks[sell_order.ticker].past10secs.append(buy_order.price)
        if len(self.stocks[sell_order.ticker].past10secs) > 10:
            self.stocks[sell_order.ticker].past10secs.popleft()

        print(f"{seller.id} sold {q} shares of {sell_order.ticker} to {buyer.id} at ${sell_order.price} per share")
    

    def get_strategy(self, ticker):
        return self.stocks[ticker].analyse_last_10()

        

