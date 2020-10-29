from cryptofeed.backends.influxdb import TradeInflux
from cryptofeed import FeedHandler
from cryptofeed.exchanges import FTX
from cryptofeed.defines import TRADES

from config import Exchange


def main(pairs):
    f = FeedHandler()
    trade_influx = TradeInflux('http://localhost:8086', 'trades', create_db=False, numeric_type=float)
    f.add_feed(FTX(channels=[TRADES], pairs=pairs, callbacks={TRADES: trade_influx}), timeout=120)
    f.run()


if __name__ == '__main__':
    _ = Exchange.load_markets()

    pairs = Exchange.symbols
    pairs = [pair for pair in pairs if pair.endswith("PERP")]
    pairs += ["ETH-BTC", "ETH-USD", "BTC-USD"]

    while True:
        try:
            main(pairs)
        except Exception as e:
            print(e)
