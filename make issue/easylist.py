import pyautogui
from functions import *


# first click on the new issue on easylist bookmark on the bookmark bar at the top of the page
def click_new_issue_easylist_on_bookmark_bar():
    pyautogui.click(x=25, y=100)



# define the function to extract the domain name from the url in the text
def extract_domain_name_from_url(url):
    domain_name = url.split("/")[2]
    return domain_name


# define the function to click on the comment box
def click_comment_box():
    pyautogui.click(x=605, y=575)
