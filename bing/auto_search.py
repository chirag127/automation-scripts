"""
auto search a list of terms in bing search engine and save the results in a csv file
"""
import pyautogui
from time import sleep
import webbrowser




terms = """how to learn python
how to learn python for beginners
how to learn python programming
how to learn python fast
how to learn python 3
how to learn python from scratch
how to learn python in 7 days
how to learn python in 30 days
how to learn python in 1 day
how to learn python for free
how to learn python for data science
how to learn python for machine learning
how to learn python in 1 week
how to learn python in 1 month
how to learn python in 1 hour
how to learn python in 1 minute
how to learn python in 1 second"""


for term in terms.splitlines():
    if not term:
        continue

    webbrowser.open_new_tab("https://www.bing.com/search?q={}".format(term))

    sleep(5)

    pyautogui.hotkey('ctrl', 'shift', 'tab')

    sleep(5)

    pyautogui.hotkey('ctrl', 'w')

    sleep(1)
