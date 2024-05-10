import pyautogui
import random
import time


while True:
    # Generate random time delay
    time_delay = random.uniform(0, 10)  # Random time delay between 0.5 and 2 seconds
    # Press Ctrl+Tab
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.scroll(370)  # Scroll up 10 "clicks"

    time.sleep(time_delay)  # Wait for 1 second

    # Simulate mouse scroll down
    pyautogui.scroll(-107)  # Scroll down 10 "clicks"


    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(time_delay)  # Wait for 1 second

    # Generate random scroll amount
    scroll_amount = random.randint(-80, 80)  # Random scroll amount between -20 and 20
    pyautogui.scroll(scroll_amount)  # Scroll by the random amount


    pyautogui.scroll(370)  # Scroll up 10 "clicks"

    time.sleep(time_delay)  # Wait for 1 second

    # Simulate mouse scroll down
    pyautogui.scroll(-107)  # Scroll down 10 "clicks"

    time.sleep(time_delay)  # Wait for 1 second
    # Generate random time delay
    time_delay = random.uniform(0, 60)  # Random time delay between 0.5 and 2 seconds
    # Press Ctrl+Tab
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(time_delay)  # Wait for 1 second
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')

    # Generate random mouse cursor movement
    screen_width, screen_height = pyautogui.size()
    new_x = random.randint(0, screen_width)
    new_y = random.randint(0, screen_height)
    pyautogui.moveTo(new_x, new_y, duration=random.uniform(0, 60))  # Move the cursor to a random position
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('up')

    # Generate random time delay
    time_delay = random.uniform(0, 60)  # Random time delay between 0.5 and 2 seconds
    # Press Ctrl+Tab
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(time_delay)  # Wait for 1 second


    # Generate random mouse cursor movement
    screen_width, screen_height = pyautogui.size()
    new_x = random.randint(0, screen_width)
    new_y = random.randint(0, screen_height)
    pyautogui.moveTo(new_x, new_y, duration=random.uniform(0, 60))  
    time.sleep(time_delay)
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
