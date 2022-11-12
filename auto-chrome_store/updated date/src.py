import urllib.request
from bs4 import BeautifulSoup


def get_html(url1: str) -> None:
    """
    This function takes a url as an argument and returns the html code of the url.
    :param url1: url of the website
    :return: html code of the url
    """
    url = urllib.request.urlopen(url1)
    content = url.read()
    soup = BeautifulSoup(content, "html.parser")
    table = soup.findAll("span", attrs={"class": "C-b-p-D-Xe h-C-b-p-D-xh-hh"})
    for row in table:
        print(row.text)


with open("auto-chrome_store/urls.txt", "r") as f:
    urls = f.readlines()
    for url in urls:
        get_html(url)
        print("\n")
