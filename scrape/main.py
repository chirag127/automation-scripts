# scape are list of URLs of blog and append the content of the urls to the  a file called all dot txt.
# file

# scrape_blog(urls)


import requests
from bs4 import BeautifulSoup

def get_urls(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        try:

            if link.get('href').startswith('http'):
                urls.append(link.get('href'))
            elif link.get('href').startswith('/'):
                urls.append(url + link.get('href'))
            else:
                # append with url domain
                domain = url.split('/')[2]
                urls.append('http://' + domain +"/" +link.get('href'))
        except:
            pass
    return urls


def scrape_blog(urls):
    for url in urls:
        try:
            print(url)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for p in soup.find_all('p'):
                with open('alla.txt', 'a',encoding='utf-8') as f:
                    f.write(p.text)
        except:
            pass

def main():
    url = 'https://www.javatpoint.com/python-tutorial'
    urls = get_urls(url)
    try:
        scrape_blog(urls)
        print('done')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()