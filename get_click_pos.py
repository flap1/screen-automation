import ctypes
import time
import pyautogui

def get_click_pos():
    try:
        while True:
            if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                x, y = pyautogui.position()
                print("clicked x: ", x, ", y: ", y)
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("KeyboardInterrupt. Finish.")

get_click_pos()