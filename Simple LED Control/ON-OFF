import pyfirmata #This has to be installed "pip install pyfirmata"
import time
import json

def OnOff():
    try:
        with open("config.json") as config_file:
            config = json.load(config_file)
        pass
    except Exception as e:
        print(e)

    board = pyfirmata.Arduino(str(config["port"]))
    oldLed = None
    while True:
        newLed = int(input(f"Please type led number from 2 to {int(config['leds'])+1}: "))

        if newLed > int(config['leds'])+1 or newLed < 2:
            newLed = int(input(f"Only numbers between 2 to {int(config['leds'])+1}: "))


        if oldLed != None:
            board.digital[oldLed].write(0)

        oldLed = newLed
        board.digital[newLed].write(1)

if __name__ == "__main__":
    OnOff()
