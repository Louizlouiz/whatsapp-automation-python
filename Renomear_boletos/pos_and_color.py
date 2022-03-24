import pyautogui as pt
from time import sleep

while True:
    pxy = pt.position()
    print(pxy, pt.pixel(pxy[0], pxy[1]))
    sleep(1)
    if pxy[0] < 1:
        break