import yfinance as yf
import httpx
import time
import os
from dotenv import load_dotenv

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI en Docker!"}

load_dotenv()



CHAT_ID = os.getenv("CHAT_ID")
TELEGRAM_URL = os.getenv("TELEGRAM_URL")

TICKER = "NVDA"

PRICE_BUY = 144.69
PRICE_SELL = 145.69
NOTIFICADO = False
INTERVALO = 1200

def enviar_mensaje(mensaje: str):
    global NOTIFICADO
    print(CHAT_ID, TELEGRAM_URL)
    payload = {"chat_id": CHAT_ID, "text": mensaje}
    try:
        response = httpx.post(TELEGRAM_URL, data=payload)
        response.raise_for_status()
        NOTIFICADO = True
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")

def verificar_precio():
    try:

        stock = yf.Ticker(TICKER)
        if stock.info is None:
            print(f"No se encontró el ticker {TICKER}")
            return None


        current_price = stock.history(period="1d")["Close"].iloc[-1]
        current_price = round(current_price, 2)

        # mensaje = f"Precio de {TICKER} ha alcanzado o superado el precio de compra: {current_price}"
        # enviar_mensaje(mensaje)
            

        return current_price
    except Exception as e:
        print(f"Error al obtener precio: {e}")
        return None
    

if __name__ == "__main__":
    while True:
        verificar_precio()
        time.sleep(INTERVALO)