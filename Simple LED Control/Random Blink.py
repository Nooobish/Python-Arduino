import pyfirmata
import time
import json
import random

def RandomBlink():
    try:
        with open("config.json") as config_file:
            config = json.load(config_file)
        pass
    except Exception as e:
        print(e)

    board = pyfirmata.Arduino(str(config["port"]))

    while True:
        led = random.randrange(2, 2+int(config["leds"]))
        print(led)

        board.digital[led].write(1)
        time.sleep(float(config["delay"]))
        board.digital[led].write(0)

if __name__ == "__main__":
    RandomBlink()
