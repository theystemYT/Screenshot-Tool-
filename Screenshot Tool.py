DO NOT STEAL THIS CODE UNLESS GIVEN PERMISSION BY THE CREATOR TO DO SO.
import pyautogui
import os
import datetime

def take_screenshot(save_directory):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(save_directory, f"screenshot_{timestamp}.png")

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    print(f"Screenshot saved: {filename}")

if __name__ == "__main__":
    save_path = input("Enter the directory to save screenshots: ").strip()
    take_screenshot(save_path)
