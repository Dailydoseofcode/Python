import pyautogui
import time
message=5
while message>0:
    time.sleep(1)
    pyautogui.typewrite("Glad to meet you!")
    time.sleep(0.5)
    pyautogui.press('enter')
    message-=1

