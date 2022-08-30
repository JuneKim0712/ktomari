import pyautogui
import pynput
import logging
import time
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener



def on_move(x, y):
    logging.info('{0} {1}'.format(x, y))

def on_click(x, y, button, pressed):
    logging.info('{0} {1} {2} {3}'.format(
        x, y, button, pressed))

def on_scroll(x, y, dx, dy):
    logging.info('{0} {1} {2} {3}'.format(
        x, y, dx, dy))

def on_press(key):
    try:
        print(key)
        if str(key) == '':
            logging.info('k\x03')
        elif str(key) == '':
            logging.info('k\x1a')
        elif str(key) == '':
            logging.info('k\x16')
        else:
            logging.info('k{0}'.format(
                key.char))
    except AttributeError:
        logging.info('k{0}'.format(
            key))
        
def on_release(key):
    if str(key) == '':
            logging.info('k\x03')
    elif str(key) == '':
        logging.info('k\x1a')
    elif str(key) == '':
        logging.info('k\x16')
    else: logging.info('k{0}'.format(
        key))
        
    logging.info('r{0}'.format(
        key))
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False
    
def Recording(device='all'):
    logging.basicConfig(filename='mouse_log.txt', 
                        level=logging.DEBUG, 
                        format='%(message)s')
    if device == 'all' or 'keyboard':
        keyboard_listener = KeyboardListener(on_press=on_press,
                                             on_release=on_release)
    if device == 'all' or 'mouse':
        mouse_listener = MouseListener(on_move=on_move, 
                                    on_click=on_click, 
                                    on_scroll=on_scroll)
    if device == 'all' or 'keyboard':keyboard_listener.start()
    if device == 'all' or 'mouse':mouse_listener.start()
    if device == 'all' or 'keyboard':keyboard_listener.join()
    if device == 'all' or 'mouse':mouse_listener.join()


Recording('keyboard')