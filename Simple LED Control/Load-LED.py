import pyfirmata
import time
import json
import random

def fullLoad():
    try:
        with open("config.json") as config_file:
            config = json.load(config_file)
        pass
    except Exception as e:
        print(e)

    board = pyfirmata.Arduino(str(config["port"]))

    loop = list(range(2, int(config["leds"]) + 2))

    if config["fromLowest"] is False:
        loop = list(reversed(loop))

    while True:
        for led in loop:
            board.digital[led].write(1)
            time.sleep(float(config["delay"]))

        for led in loop:
            board.digital[led].write(0)

        time.sleep(float(config["fullLoadResetDelay"]))
      
 if __name__ == "__main__":
    RandomBlink()
