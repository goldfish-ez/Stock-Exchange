import random
import time
import matplotlib.pyplot as plt
import pandas as pd
from trader import Trader
from stock import Stock
from exchange import Exchange
from share import Share

money_data = pd.DataFrame(columns=["Trader", "Time", "Money"])
stock_price_data = pd.DataFrame(columns=["Time", "REL", "AIR", "JIO"])

stock_exchange = Exchange()
stock1 = Stock(stock_exchange, 12.90, "REL")
stock2 = Stock(stock_exchange, 11.40, "AIR")
stock3 = Stock(stock_exchange, 10.80, "JIO")

stock_exchange.stocks = {"REL": stock1, "AIR": stock2, "JIO": stock3}


for i in range(5):
    trader = Trader(i, random.randint(20000, 50000), random.randint(20000, 50000), {}, stock_exchange)
    for _ in range(random.randint(1000, 20000)):
        stock = random.choice([stock1, stock2, stock3])
        share = Share(stock, i)
        trader.portfolio.setdefault(stock.ticker, []).append(share)
    stock_exchange.traders[i] = trader

for j in range(50):
    for i in range(5):
        stock = random.choice([stock1, stock2, stock3])
        order_type = stock_exchange.traders[i].strategy(stock.ticker)
        price = random.randint(int(stock.cur_price - 2), int(stock.cur_price + 2))
        quantity = random.randint(100, 400)
        timestamp = time.time()

        stock_exchange.traders[i].place_limit_order(
            type=order_type, quantity=quantity,
            ticker=stock.ticker, price=price, time=timestamp
        )

        money_data = pd.concat([money_data, pd.DataFrame([{
            "Trader": i,
            "Time": j,
            "Money": stock_exchange.traders[i].trading_balance
        }])], ignore_index=True)


    stock_price_data = pd.concat([stock_price_data, pd.DataFrame([{
        "Time": j,
        "REL": stock1.cur_price,
        "AIR": stock2.cur_price,
        "JIO": stock3.cur_price
    }])], ignore_index=True)


for ticker in ["REL", "AIR", "JIO"]:
    print(stock_exchange.stocks[ticker].past10secs)

# # Plot balance for each trader
# for i in range(5):
#     trader_data = money_data[money_data["Trader"] == i]
#     plt.figure(figsize=(8, 4))
#     plt.plot(trader_data["Time"], trader_data["Money"], marker='o')
#     plt.title(f"Trader {i} - Money Over Time")
#     plt.xlabel("Time")
#     plt.ylabel("Trading Balance")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()

# # Plot stock prices over time
# for ticker in ["REL", "AIR", "JIO"]:
#     plt.figure(figsize=(8, 4))
#     plt.plot(stock_price_data["Time"], stock_price_data[ticker], label=ticker, marker='o')
#     plt.title(f"{ticker} - Price Over Time")
#     plt.xlabel("Time")
#     plt.ylabel("Price")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()























# # from trader import Trader
# # from stock import Stock
# # from exchange import Exchange
# # from share import Share
# # from order import Order, BuyOrder, SellOrder
# # import random
# # import time
# # import matplotlib.pyplot as plt
# # import pandas as pd

# # # money_data = pd.DataFrame({"Trader" : [], "Time" : [], "Money" : []})


# # # stock_exchange = Exchange()

# # # stock1 = Stock(stock_exchange, 12.90, "REL")
# # # stock2 = Stock(stock_exchange, 11.40, "AIR")
# # # stock3 = Stock(stock_exchange, 10.80, "JIO")

# # # stock_exchange.stocks["REL"] = stock1
# # # stock_exchange.stocks["AIR"] = stock2
# # # stock_exchange.stocks["JIO"] = stock3


# # # for i in range(10):
# # #     trader = Trader(i, random.randint(20000, 50000), random.randint(20000, 50000), {}, stock_exchange)
# # #     for j in range(random.randint(1000, 20000)):
# # #         number = random.randint(1, 3)
# # #         if number == 1:
# # #             share = Share(stock1, i)
# # #         elif number == 2:
# # #             share = Share(stock2, i)
# # #         else:
# # #             share = Share(stock3, i)

# # #         if share.stock.ticker in trader.portfolio:
# # #             trader.portfolio[share.stock.ticker].append(share)
# # #         else:
# # #             trader.portfolio[share.stock.ticker] = [share]
# # #     stock_exchange.traders[i] = trader
# # #     money_data[trader.id] = []
# # #     # print(trader.balance, trader.trading_balance)
    


# # # for j in range(100):
# # #     for i in range(10):
# # #         number = random.randint(1, 2)
# # #         n = random.randint(1, 3)
# # #         if n == 1:
# # #             stock = stock1
# # #         elif n == 2:
# # #             stock = stock2
# # #         else:
# # #             stock = stock3
# # #         if number == 1:
# # #             stock_exchange.traders[i].place_limit_order(type = "BID", quantity = random.randint(100, 400), 
# # #                                                         ticker = stock.ticker, time= time.time(), 
# # #                                                         price = random.randint(int(stock.cur_price - 2), int(stock.cur_price + 2)))
            
# # #         else:
# # #             stock_exchange.traders[i].place_limit_order(type = "OFFER", quantity = random.randint(100, 400), 
# # #                                                         ticker = stock.ticker, time= time.time(), 
# # #                                                         price = random.randint(int(stock.cur_price - 2), int(stock.cur_price + 2)))


# # #         money_data = pd.concat(money_data, pd.DataFrame({"Trader" : i, "Time" : j, "Money" : stock_exchange.traders[i].trading_balance}))


# # # plt.plot(money_data)
# # # plt.show()



# # money_data = pd.DataFrame(columns=["Trader", "Time", "Money"])

# # # Setup stock exchange and stocks
# # stock_exchange = Exchange()
# # stock1 = Stock(stock_exchange, 12.90, "REL")
# # stock2 = Stock(stock_exchange, 11.40, "AIR")
# # stock3 = Stock(stock_exchange, 10.80, "JIO")
# # stock_exchange.stocks = {"REL": stock1, "AIR": stock2, "JIO": stock3}

# # # Create traders and assign random shares
# # for i in range(5):
# #     trader = Trader(i, random.randint(20000, 50000), random.randint(20000, 50000), {}, stock_exchange)
    
# #     for _ in range(random.randint(1000, 20000)):
# #         stock = random.choice([stock1, stock2, stock3])
# #         share = Share(stock, i)
# #         trader.portfolio.setdefault(stock.ticker, []).append(share)

# #     stock_exchange.traders[i] = trader

# # # Simulate 100 rounds of trading
# # for j in range(50):
# #     for i in range(5):
# #         stock = random.choice([stock1, stock2, stock3])
# #         order_type = random.choice(["BID", "OFFER"])
# #         price = random.randint(int(stock.cur_price - 2), int(stock.cur_price + 2))
# #         quantity = random.randint(100, 400)
# #         timestamp = time.time()

# #         stock_exchange.traders[i].place_limit_order(
# #             type=order_type, quantity=quantity,
# #             ticker=stock.ticker, price=price, time=timestamp
# #         )

# #         # Append trader's balance to the DataFrame
# #         money_data = pd.concat([money_data, pd.DataFrame([{
# #             "Trader": i,
# #             "Time": j,
# #             "Money": stock_exchange.traders[i].trading_balance
# #         }])], ignore_index=True)

# # # Pivot data to plot each trader's money across time
# # pivoted = money_data.pivot(index="Time", columns="Trader", values="Money")
# # pivoted.plot(title="Trader Money over Time", figsize=(12, 6))
# # plt.xlabel("Time")
# # plt.ylabel("Money")
# # plt.legend(title="Trader")
# # plt.grid(True)
# # plt.tight_layout()
# # plt.show()

# import random
# import time
# import matplotlib.pyplot as plt
# import pandas as pd
# from trader import Trader
# from stock import Stock
# from exchange import Exchange
# from share import Share
# from order import Order, BuyOrder, SellOrder

# # Setup
# money_data = pd.DataFrame(columns=["Trader", "Time", "Money"])
# stock_exchange = Exchange()
# stock1 = Stock(stock_exchange, 12.90, "REL")
# stock2 = Stock(stock_exchange, 11.40, "AIR")
# stock3 = Stock(stock_exchange, 10.80, "JIO")
# stock_exchange.stocks = {"REL": stock1, "AIR": stock2, "JIO": stock3}

# # Create 5 traders and assign shares randomly
# for i in range(5):
#     trader = Trader(i, random.randint(20000, 50000), random.randint(20000, 50000), {}, stock_exchange)
#     for _ in range(random.randint(1000, 20000)):
#         stock = random.choice([stock1, stock2, stock3])
#         share = Share(stock, i)
#         trader.portfolio.setdefault(stock.ticker, []).append(share)
#     stock_exchange.traders[i] = trader

# # Simulate 50 trading rounds
# for j in range(50):
#     for i in range(5):
#         stock = random.choice([stock1, stock2, stock3])
#         order_type = random.choice(["BID", "OFFER"])
#         price = random.randint(int(stock.cur_price - 2), int(stock.cur_price + 2))
#         quantity = random.randint(100, 400)
#         timestamp = time.time()

#         stock_exchange.traders[i].place_limit_order(
#             type=order_type, quantity=quantity,
#             ticker=stock.ticker, price=price, time=timestamp
#         )

#         money_data = pd.concat([money_data, pd.DataFrame([{
#             "Trader": i,
#             "Time": j,
#             "Money": stock_exchange.traders[i].trading_balance
#         }])], ignore_index=True)

# # Plot balance and portfolio for each trader
# for i in range(5):
#     # Trader Money Over Time
#     trader_data = money_data[money_data["Trader"] == i]
#     plt.figure(figsize=(8, 4))
#     plt.plot(trader_data["Time"], trader_data["Money"], marker='o')
#     plt.title(f"Trader {i} - Money Over Time")
#     plt.xlabel("Time")
#     plt.ylabel("Trading Balance")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()

#     # Trader Portfolio
#     portfolio = stock_exchange.traders[i].portfolio
#     portfolio_counts = {ticker: len(shares) for ticker, shares in portfolio.items()}
    
#     # You can use either pie or bar chart:
#     # Pie Chart
#     plt.figure(figsize=(5, 5))
#     plt.pie(portfolio_counts.values(), labels=portfolio_counts.keys(), autopct='%1.1f%%')
#     plt.title(f"Trader {i} - Share Portfolio Distribution")
#     plt.tight_layout()
#     plt.show()
    
#     # Bar Chart Alternative
#     # plt.figure(figsize=(6, 4))
#     # plt.bar(portfolio_counts.keys(), portfolio_counts.values())
#     # plt.title(f"Trader {i} - Share Portfolio")
#     # plt.xlabel("Stock Ticker")
#     # plt.ylabel("Number of Shares")
#     # plt.tight_layout()
#     # plt.show()



    
            
        
        
    