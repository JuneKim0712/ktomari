import pyautogui 

def click(button):
    print(1)
    pyautogui.mouseDown(button=button)
    pyautogui.mouseUp(button=button)

click('left')