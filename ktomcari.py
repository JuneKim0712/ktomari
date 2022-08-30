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
    global globalDevice, keyboard_listener, mouse_listener
    if str(key) == 'Key.esc':
        if globalDevice == ('keyboard' or 'all'):
            keyboard_listener.stop()
        if globalDevice == ('mouse' or 'all'):
            mouse_listener.stop()
        return
    if globalDevice == 'keyboard' or 'all':
        try: 
            if str(key.char) == '':
                logging.info('^c')
                return
            elif str(key.char) == '':
                logging.info('^z')
                return
            elif str(key.char) == '':
                logging.info('^v')
                return
            logging.info('k{0}'.format(
                            key.char))
        except AttributeError:
            logging.info('k{0}'.format(
                        key))
    return
        
def on_release(key):
    return
    
def Recording(device='all'):
    global globalDevice, keyboard_listener, mouse_listener
    
    globalDevice = device
    
    logging.basicConfig(filename='log.txt', 
                        level=logging.DEBUG, 
                        format='%(message)s')
    keyboard_listener = KeyboardListener(on_press=on_press,
                                            on_release=on_release)
    if device == ('all' or 'mouse'):
        mouse_listener = MouseListener(on_move=on_move, 
                                    on_click=on_click, 
                                    on_scroll=on_scroll)
    keyboard_listener.start()
    if device == ('all' or 'mouse'):mouse_listener.start()
    keyboard_listener.join()
    if device == ('all' or 'mouse'):
        mouse_listener.join()
    print('recorded successfully')
    return

Recording('keyboard')