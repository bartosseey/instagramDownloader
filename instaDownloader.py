import requests
from bs4 import BeautifulSoup





if __name__=="__main__":
    url = 'https://www.instagram.com/paninaa.d/'
    req = requests.get(url)



    soup = BeautifulSoup(req.text, 'lxml')

    print(soup.prettify())