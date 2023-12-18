import pyautogui
import random
import sys
import keyboard

coordinates = {
    "xCoord":0,
    "yCoord":0,
}

def WaitForStart():
    print("Move cursor to wanted spot (on top of Knight and coin pouch.)")
    print("Press CTRL to start clicking.")
    print("Hold ESC to shutdown.")
    
    while True:
        if (keyboard.is_pressed('left ctrl')):
            coordinates["xCoord"], coordinates["yCoord"] = pyautogui.position()
            clicking()

def clicking():
    while True:
        one_cycle = random.randint(75, 110)
        for _ in range(one_cycle):
            if keyboard.is_pressed('esc'):
                print("Exitting...")
                pyautogui.PAUSE = 2
                sys.exit()
            pyautogui.click(coordinates["xCoord"], coordinates["yCoord"], button='left')
            delay = random.randint(301, 399) 
            pyautogui.PAUSE = delay / 1000
        openPouches()

def openPouches():
    pyautogui.press('f2')
    pyautogui.PAUSE = 0.2
    pyautogui.click(coordinates["xCoord"], coordinates["yCoord"], button='left', clicks=3, interval=0.2)
    pyautogui.PAUSE = 0.4
    pyautogui.press('f2')

if __name__ == "__main__":
    WaitForStart()
