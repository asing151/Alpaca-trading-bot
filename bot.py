import alpaca_trade_api as tradeapi

class Martingale(object):
    def _init_(self):
        self.key = 'PKNUU4XAHJRALL6RB7ZP'
        self.secret = 'Av4xZvdHCTDolXglayPCUVuOOi6vZCy55pAxvxum'
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST('PKNUU4XAHJRALL6RB7ZP', 'Av4xZvdHCTDolXglayPCUVuOOi6vZCy55pAxvxum', self.alpaca_endpoint)
        self.symbol = 'SPY'
        self.current_order = None
        self.last_price = 1

        try:
            self.position = int(self.api.get_position(self.symbol).qty)

        except:
            self.position = 0

    def submit_order(self, target):
        if self.current_order is not None:
            self.api.cancel_order(self.current_order.id)

        delta = target - self.position
        if delta == 0:
            return 
        print(f'Processing order for {target} shares')

        if delta > 0:
            buy_quantity = delta
            if self.position < 0:
                buy_quantity = min(abs(self.position), buy_quantity)
            print(f'buying {buy_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol, buy_quantity, 'buy', 'limit', 'day', self.last_price)


        elif delta < 0:
            sell_quantity = abs(delta)
            if self.position > 0:
                sell_quantity = min(sell_quantity, abs(self.position))
                
            print(f'selling {sell_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol, sell_quantity, 'sell', 'limit', 'day', self.last_price)
                
if __name__ == '__main__':
    t = Martingale()
    t.submit_order(3)



