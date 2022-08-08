#código que se conecta a outros dispositivos em uma rede local, como uma lâmpada, por meio de uma API
#usamos o método PUT para enviar uma mensagem para a nossa lâmpada, desligando-a.
import os
import requests
import time

USERNAME = os.getenv("USERNAME")
IP = os.getenv("IP")
URL = f"http://{IP}/api/{USERNAME}/lights/1/state"

while True:
    requests.put(URL, json={"bri": 254, "on": True})
    time.sleep(1)
    requests.put(URL, json={"on": False})
    time.sleep(1)