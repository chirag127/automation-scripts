from time import sleep
import pyautogui
import keyboard

def right_click_and_select_option(x: int, y: int, option_x: int, option_y: int) -> None:
    pyautogui.rightClick(x, y)
    sleep(0.5)
    pyautogui.click(option_x, option_y)
    sleep(0.3)
    pyautogui.click(1096, 565)

def main() -> None:
    current_x, current_y = pyautogui.position()
    option_x, option_y = current_x + 103, current_y + 226
    right_click_and_select_option(current_x, current_y, option_x, option_y)
    pyautogui.click(current_x, current_y)

if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("a"):
            main()
        else:
            sleep(0.1)
