import websocket
import json


def on_message(ws, message):
    print(json.loads(message))


def on_error(ws, error):
    print(ws)
    print(error)


def on_close(ws):
    print(ws)
    print("### closed ###")


ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/maticusdt@bookTicker",
                            on_message=on_message,
                            on_error=on_error)
ws.run_forever()