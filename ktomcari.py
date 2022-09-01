import pyautogui
import pynput
import logging
import time
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener


pyautogui.PAUSE = 0.0001

def on_move(x, y):
    logging.info('m{0} {1}e'.format(x, y))

def on_click(x, y, button, pressed):
    logging.info('p{0} {1}e{2}z{3}'.format(
        x, y, button, pressed))

def on_scroll(x, y, dx, dy):
    logging.info('s{0} {1}e{2}p{3}'.format(
        x, y, dx, dy))

def on_press(key):
    global globalDevice, keyboard_listener, mouse_listener
    if str(key) == 'Key.esc':
        keyboard_listener.stop()
        if globalDevice == 'mouse' or globalDevice == ('all'):
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
    
    file = open('log.txt', 'w').close()
    
    logging.basicConfig(filename='log.txt', 
                        level=logging.DEBUG, 
                        format='%(message)s')
    keyboard_listener = KeyboardListener(on_press=on_press,
                                            on_release=on_release)
    if (device == 'all' or device =='mouse'):
        mouse_listener = MouseListener(on_move=on_move, 
                                    on_click=on_click, 
                                    on_scroll=on_scroll)
    keyboard_listener.start()
    if (device == 'all' or device =='mouse'): mouse_listener.start()
    keyboard_listener.join()
    if (device == 'all' or  device == 'mouse'):
        mouse_listener.join()
    print('recorded successfully')
    return

def execute():
    logfile=open('log.txt', 'r')
    while True:
        line=logfile.readline()
        if not line:
            break
        else:
            if line[0] == 'p'  or line[0] == 'm'or line[0] == 's':
                x=line[1:line.index(' ')]
                y=line[line.index(' ')+1:line.index('e')]
                pyautogui.moveTo(int(x), int(y))
                if line[0] == 'p':
                    if line[line.index('.')+1] == 'r':
                        if line[line.index('z')+1] == 'T':
                            pyautogui.mouseDown(button='right')
                        else:
                            pyautogui.mouseUp(button='right')
                    elif line[line.index('z')+1] == 'T':
                        pyautogui.mouseDown(button='left')
                    else:
                        pyautogui.mouseUp(button='left')
                
    print('finished')
    
    
Recording('all')
execute()