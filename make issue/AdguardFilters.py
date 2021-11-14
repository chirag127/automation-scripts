
#! python3
# make a program that will make a github issue when user press "z" key on the keyboard on https://github.com/AdguardTeam/AdguardFilters/issues/new
import pyautogui
from urllib.parse import urlparse
import clipboard
from functions import *
import webbrowser

# first we will click on the "z" key
# click on the url bar at the top of the page
# copy the url from the url bar using the pyautogui library by pressing the "ctrl" key + "c"
# then we will paste the url into the url variable using the clipboard library by clipboard.paste()
# we will then parse the url using the urlparse library
# we will the domain name from the url using the urlparse library
# we will then type click on the create new issue bookmark on the top left of the page at the bookmark bar
# we will wait for the new issue page to load
# we will types the title of the issue as the domain name using pyautogui.typewrite()
# we will then type click on the body of the issue using pyautogui.click()
# we will then type the content of the issue using pyautogui.typewrite() with the url variable using pyautogui.typewrite()
# we will click in the screenshot area using pyautogui.click()
# we will then paste the screenshot using pyautogui.hotkey()
# we will then move to the next tab using pyautogui.hotkey()


# first open the adguard filters new issues url
# url https://github.com/AdguardTeam/AdguardFilters/issues/new
def open_adguard_filter_new_issues_url():
    webbrowser.open("https://github.com/AdguardTeam/AdguardFilters/issues/new")


def main():

    # click_url_bar()

    wait(0.2)

    copyselectedtext()

    # get the url of the website by using the clipboard
    url = clipboard.paste()

    # parse the url to get the domain name
    domain = urlparse(url).netloc

    wait(0.1)

    close_tab()

    wait(0.1)

    open_adguard_filter_new_issues_url()

    # wait for to load the issue page
    wait(3)

    pyautogui.typewrite(domain)

    # wait for to load the issue page
    wait(0.1)

    click_body()

    wait(0.1)

    # type the issue with the url of the issue webpage
    pyautogui.typewrite(f"""**Issue URL (Ads/Annoyance)**:  `{url}`


<details><summary>Screenshots:</summary>









</details><br/>

<details><summary>System configuration:</summary>

![image](https://user-images.githubusercontent.com/76880977/141497551-099fafbf-933f-44c7-956a-f88fc1bcb5d5.png)

</details><br/>""")

    wait(0.1)

    click_screenshot_holder()

    wait(0.1)

    # press windows + 2 to paste the screenshot
    pyautogui.hotkey('win', 'num2')

    wait(0.1)


    open_last_closed_tab()


    wait(0.1)

    close_tab()


if __name__ == "__main__":

    # make a infinite loop that will wait for the "z" key to be pressed
    while True:

        wait_for_do_key()

        main()
