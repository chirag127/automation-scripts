from functions import *


# create issue on the https://github.com/AdguardTeam/AdguardFilters/issues/new?assignees=&template=bug_report.yml


if __name__ == "__main__":

    pyautogui.hotkey("alt", "d")

    copyselectedtext()

    webbrowser.open(
        "https://github.com/chirag127/test/issues/new?assignees=&template=bug_report.yml"
    )

    sleep(3)

    pyautogui.typewrite(type_domain)
