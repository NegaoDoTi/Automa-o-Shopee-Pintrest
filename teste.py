from pynput.mouse import Controller
from time import sleep


mouse = Controller()

while True:

    x, y = mouse.position
    print(f"X:{x}, Y:{y}")
    sleep(0.2)