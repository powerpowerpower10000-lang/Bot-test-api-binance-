import ccxt
import os
import time
import logging
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def print_status(ok, message):
    if ok:
        print(r"""
   ____  _   _  _   _  _____  _   _ 
  / ___|| | | || \ | || ____|| \ | |
 | |    | | | ||  \| ||  _|  |  \| |
 | |___ | |_| || |\  || |___ | |\  |
  \____| \___/ |_| \_||_____||_| \_|

        ✅ CONECTADO
""")
    else:
        print(r"""
   _____  ____   ____   ___  ____  
  | ____||  _ \ |  _ \ |_ _|/ ___| 
  |  _|  | |_) || |_) | | || |     
  | |___ |  _ < |  _ <  | || |___  
  |_____||_| \_\|_| \_\|___|\____|

        ❌ ERROR
""")
    print(f"→ {message}\n")

def connect():
    try:
        exchange = ccxt.binance({
            'apiKey': API_KEY,
            'secret': API_SECRET,
            'enableRateLimit': True,
        })

        exchange.set_sandbox_mode(True)

        exchange.urls['api'] = {
            'public': 'https://testnet.binance.vision/api',
            'private': 'https://testnet.binance.vision/api',
        }

        balance = exchange.fetch_balance()
        print_status(True, "Conectado a Binance Testnet")
        return exchange

    except Exception as e:
        print_status(False, str(e))
        return None

def loop():
    while True:
        try:
            exchange = connect()

            if exchange:
                logging.info("Conexión OK")
            else:
                logging.error("Fallo conexión")

        except Exception as e:
            logging.error(f"Error loop: {e}")

        time.sleep(30)

if __name__ == "__main__":
    loop()
