import pyautogui
import webbrowser

# define a function that will go to next tab using pyautogui.hotkey('ctrl', 'tab')


def go_to_next_tab():

    pyautogui.hotkey('ctrl', 'tab')


# click on the new issue button on the bookmark bar at the top of the page at X,Y coordinates of the screen


def click_new_issue():

    pyautogui.click(x=25, y=100)

# define a function that will click on the url bar at the top of the page


def click_url_bar():

    pyautogui.click(x=400, y=65)


# define a function that will copy the url from the url bar using the pyautogui library by pressing the "ctrl" key + "c"
def copyselectedtext():

    pyautogui.hotkey('ctrl', 'c')


# type click on the body of the issue using pyautogui.click()
def click_body():

    pyautogui.click(x=605, y=575)


# click place of screenshot holder
def click_screenshot_holder():
    pyautogui.click(x=566, y=650)


# move focus out of the comment box
def move_focus_out_of_comment_box():
    pyautogui.click(x=20, y=575)


# define a function that will open the url in the default browser
def open_url(url):

    webbrowser.open(url)

# define a function that will click at the specified coordinates


def click_at_coordinates(x, y):

    pyautogui.click(x=x, y=y)


# define a function that will type the text
def type_text(text):

    pyautogui.typewrite(text)


def close_tab():

    pyautogui.hotkey('ctrl', 'w')


# define a function that will open the last closed tab
# open last closed tab
def open_last_closed_tab():

    pyautogui.hotkey('ctrl', 'shift', 't')


# define a function that will click on the title of the issue
def click_title():

    pyautogui.click(x=420, y=420)
