import ccxt


Exchange = ccxt.ftx({
    'apiKey': "",
    'secret': "",
    'timeout': 5000,
    'enableRateLimit': True,
})

_ = Exchange.load_markets()

PAIRS = Exchange.symbols
PAIRS = [pair for pair in PAIRS if pair.endswith("PERP")]
PAIRS += ["ETH/BTC", "ETH/USD", "BTC/USD"]
