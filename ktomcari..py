import pyautogui
import pynput
from pynput.mouse import Listener
import logging
import time

logging.basicConfig(filename='mouse_log.txt', level=logging.DEBUG, format='%(message)s')
def on_move(x, y):
    logging.info('{0} {1}'.format(x, y))

def on_click(x, y, button, pressed):
    logging.info('{0} {1} {2} {3}'.format(x, y, button, pressed))

def on_scroll(x, y, dx, dy):
    logging.info('{0} {1} {2} {3}'.format(x, y, dx, dy))

with Listener(on_move=on_move, on_scroll=on_scroll, on_click=on_click) as listener:
    listener.join()