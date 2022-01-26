from bs4 import BeautifulSoup
import urllib.request



def get_html(url1):
    url = urllib.request.urlopen(url1)
    content = url.read()
    soup = BeautifulSoup(content, 'html.parser')

    table = soup.findAll('span',attrs={"class":"C-b-p-D-Xe h-C-b-p-D-xh-hh"})
    for row in table:
        print(row.text)



    # Another way to retrieve tables:
    # table = soup.select('div[class="content-question"]')


with open("urls.txt", "r") as f:
    urls = f.readlines()
    for url in urls:
        get_html(url)
        print("\n")