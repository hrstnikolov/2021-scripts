import pyautogui
import os
from datetime import datetime

os.chdir(r'C:\Users\a1056968\Desktop')
img = pyautogui.screenshot()
img.save(f'{datetime.now().strftime("%Y%m%d")}.jpg')
