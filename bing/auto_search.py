"""
auto search a list of terms in bing search engine and save the results in a csv file
"""
import pyautogui
from time import sleep
import webbrowser



terms = """What is the meaning of the word "serendipity"?
Who discovered the first antibiotic and what was it called?
Who was the first woman to win a Nobel Prize, and in what field was the prize awarded?
What is the Higgs boson, and why is it important in physics?
What is the name of the algorithm used by Google's search engine?
Who invented the first digital computer, and what year was it invented?
What is the difference between a gene and a chromosome?
What is the formula for calculating the area of a circle, and who discovered it?
What is the significance of the painting "The Persistence of Memory" by Salvador Dali?
What is the difference between a meteor, a meteorite, and an asteroid?"""


for term in terms.splitlines():
    if not term:
        continue

    webbrowser.open_new_tab("https://www.bing.com/search?q={}".format(term))
    sleep(1)
