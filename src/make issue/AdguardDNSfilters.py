import pyautogui
from functions import *
import clipboard
from urllib.parse import urlparse
from time import sleep

# open adguard dns filter url in browser https://github.com/AdguardTeam/AdGuardSDNSFilter/issues/new


def open_adguard_dns_filter_url():
    webbrowser.open('https://github.com/chirag127/test/issues/new')
    sleep(5)


def wait_for_do_key():
    while True:
        if pyautogui.keyDown('d'):
            break
        else:
            sleep(1)


while True:

    wait_for_do_key()

    pyautogui.hotkey('alt', 'd')

    copyselectedtext()

    sleep(0.5)

    # get the url of the website by using the clipboard
    url = clipboard.paste()

    # parse the url to get the domain name
    domain = urlparse(url).netloc

    open_adguard_dns_filter_url()

    pyautogui.typewrite(domain)

    sleep(0.2)

    click_body()

    pyautogui.hotkey('ctrl', 'a')

    sleep(0.2)

    pyautogui.typewrite(f"""### Steps to reproduce
<!--- Provide a link to a live example or a clear set of steps to reproduce the issue-->
1. Go to {url}.
2. See bug.

### Expected behavior
<!--- Tell us what should happen -->
Not Blocked

### Actual behavior
<!--- Tell us what happens instead -->
Blocked""")

    sleep(0.2)

    click_title()

    pyautogui.press('enter')
