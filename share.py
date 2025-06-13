# Should have access to the stock

class Share:
    def __init__(self, ticker, owner_id):
        self.ticker = ticker
        self.owner_id = owner_id
        self.engaged = False