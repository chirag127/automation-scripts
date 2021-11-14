import pyautogui
from functions import *
import clipboard
from urllib.parse import urlparse

# open adguard dns filter url in browser https://github.com/AdguardTeam/AdGuardSDNSFilter/issues/new


def open_adguard_dns_filter_url():
    open_url('https://github.com/chirag127/test/issues/new')
    wait(5)


def wait_for_do_key():
    while True:
        if pyautogui.keyDown('d'):
            break
        else:
            wait(1)


while True:

    wait_for_do_key()

    click_url_bar()

    copyselectedtext()

    wait(0.5)

    # get the url of the website by using the clipboard
    url = clipboard.paste()

    # parse the url to get the domain name
    domain = urlparse(url).netloc

    open_adguard_dns_filter_url()

    pyautogui.typewrite(domain)

    wait(0.2)

    click_body()

    pyautogui.hotkey('ctrl', 'a')

    wait(0.2)

    type_text(f"""### Steps to reproduce
<!--- Provide a link to a live example or a clear set of steps to reproduce the issue-->
1. Go to {url}.
2. See bug.

### Expected behavior
<!--- Tell us what should happen -->
Not Blocked

### Actual behavior
<!--- Tell us what happens instead -->
Blocked""")

    wait(0.2)

    click_title()

    pyautogui.press('enter')
