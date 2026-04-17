import pyautogui, time, random

width, height = pyautogui.size()

for i in range(random.randint(6,20)):
    pyautogui.moveTo(random.randint(0, width), random.randint(0, height))
    time.sleep(0.75)