import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def openWeb():
    #dir to chromedriver
    s=Service("C:\ChromeDriver\chromedriver.exe")

    #start windows maximized to allow scroll
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=s, options=options)
    #launch chrome with filmweb open
    driver.get('https://www.instagram.com/paninaa.d/')
    time.sleep(10)
    html = driver.page_source
    driver.close()
    return html


if __name__=="__main__":
    html = openWeb()

    soup = BeautifulSoup(html, 'html.parser')

    result = []

    images = soup.find_all('img', src="True")

    for i in images:
        result.append(i['src'])

    print(result)

