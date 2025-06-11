# Should have access to the exchange

class Trader:
    def __init__(self, id, balance, trading_balance, portfolio, exchange):
        self.id = id
        self.balance = balance
        self.trading_balance = trading_balance
        self.portfolio = portfolio
        self.exchange = exchange

    def add_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.trading_balance += amount
            print(f"Successfully added ${amount} to the trading account!")
        else:
            print("Not enough balance!")

    def deduct_money(self, amount):
        if self.trading_balance >= amount:
            self.trading_balance -= amount
            return True
        else:
            print(f"Not enough funds!")
            return False

    def receive_money(self, amount):
        self.trading_balance += amount
        return True

    def sell_share(self, quantity, ticker):
        if ticker not in self.portfolio:
            print(f"No shares of {ticker}!")
            return False
        else:
            if len(self.portfolio[ticker]) < quantity:
                print(f"Not enough shares of {ticker}!")
                return False
            else:
                shares = self.portfolio[ticker][-quantity - 1 : ]
                self.portfolio[ticker] = self.portfolio[ticker][-quantity - 1 : ]
                return shares
            
    def buy_share(self, shares, ticker):
        if ticker not in self.portfolio:
            self.portfolio[ticker] = shares
        else:
            self.portfolio[ticker] += shares

        for share in shares:
            share.owner_id = self.id
        return True

    def place_limit_order(self, type, quantity, ticker, time, price):
        if type == "BID":
            if self.trading_balance < price * quantity:
                print("Not enough funds!")
            else:
                print(f"{self.id} placed a bid on {ticker} for {quantity} shares at ${price}")
                self.exchange.place_bid(self, quantity, ticker, time, price)
            pass
        else:
            if len(self.portfolio[ticker]) < quantity:
                print(f"Not enough shares of {ticker}!")
            else:
                shares = self.sell_share(quantity, ticker)
                print(f"{self.id} placed an offer on {ticker} for {quantity} shares at ${price}")
                self.exchange.place_offer(self, quantity, ticker, time, price, shares)
            pass


    def strategy(self, ticker):
        return self.exchange.get_strategy(ticker)

    
