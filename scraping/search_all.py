import os
import pyautogui
from time import sleep
import webbrowser




# Insurance	$54.91
# Loans	$44.28
# Mortgage	$47.12
# Attorney	$47.07
# Credit	$36.06
# Lawyer	$42.51
# Donate	$42.02
# Degree	$40.61
# Hosting	$31.91
# Claim	$45.51
# Conference Call	$42.05
# Trading	$33.19
# Software	$35.29
# Recovery	$42.03
# Transfer	$29.86
# Gas/Electicity	$54.62
# Classes	$35.04
# Rehab	$33.59
# Treatment	$37.18
# Cord Blood	$27.80

string = """buy insurance online
fartificial intelligence course
course web development
data science course
course machine learning
course python
course java
course javascript
course c++
c++ course
course c#
course c
course c programming
course c sharp
course c language
course c programming language
course c programming tutorial
course c programming for beginners
best code assistant
best ai copywriter
best ai copywriting
best ai writer
best ai content writer
best ai code assistant"""


search_term = string.splitlines()
for i in search_term:

    # webbrowser.open("https://neeva.com/search?q="+i+" book summary")

    webbrowser.open("https://www.bing.com/search?q="+i+" online&authuser=5")

    sleep(5)

    pyautogui.hotkey('ctrl', 'shift', 'tab')

    sleep(5)

    pyautogui.hotkey('ctrl', 'w')

    sleep(1)
