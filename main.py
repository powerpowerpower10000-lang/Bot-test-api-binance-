import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

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

def test_connection():
    try:
        exchange = ccxt.binance({
            'apiKey': API_KEY,
            'secret': API_SECRET,
            'enableRateLimit': True,
        })

        # activar testnet
        exchange.set_sandbox_mode(True)

        exchange.urls['api'] = {
            'public': 'https://testnet.binance.vision/api',
            'private': 'https://testnet.binance.vision/api',
        }

        balance = exchange.fetch_balance()

        if balance:
            print_status(True, "Conexión exitosa a Binance Testnet")
        else:
            print_status(False, "Sin respuesta de balance")

    except Exception as e:
        print_status(False, str(e))

if __name__ == "__main__":
    test_connection()
