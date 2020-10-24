from cryptofeed.backends.influxdb import TradeInflux
from cryptofeed import FeedHandler
from cryptofeed.exchanges import FTX
from cryptofeed.defines import TRADES

from config import *


def main():
    f = FeedHandler()
    trade_influx = TradeInflux('http://localhost:8086', 'trades', numeric_type=float)
    f.add_feed(FTX(channels=[TRADES], pairs=PAIRS, callbacks={TRADES: trade_influx}), timeout=120)
    f.run()


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception:
            continue
