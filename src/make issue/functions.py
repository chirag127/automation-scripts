import pyautogui
import webbrowser

# define a function that will go to next tab using pyautogui.hotkey('ctrl', 'tab')
def go_to_next_tab():

    pyautogui.hotkey('ctrl', 'tab')


# click on the new issue button on the bookmark bar at the top of the page at X,Y coordinates of the screen
def click_new_issue():

    pyautogui.click(x=25, y=100)


# define a function that will copy the url from the url bar using the pyautogui library by pressing the "ctrl" key + "c"
def copyselectedtext():

    pyautogui.hotkey('ctrl', 'c')


# type click on the body of the issue using pyautogui.click()
def click_body():

    pyautogui.click(x=600, y=580)


# click place of screenshot holder
def click_screenshot_holder():
    pyautogui.click(x=600, y=630)


def close_tab():
    pyautogui.hotkey('ctrl', 'w')


# define a function that will open the last closed tab
# open last closed tab
def open_last_closed_tab():

    pyautogui.hotkey('ctrl', 'shift', 't')


# define a function that will click on the title of the issue
def click_title():

    pyautogui.click(x=420, y=420)
