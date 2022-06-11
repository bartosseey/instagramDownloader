from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import os
import wget


import account



def open_web(profile):
    chpath = account.chromePath
    s=Service(chpath)

    name = account.username()
    passw = account.password()

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=s, options=options)
    driver.get(profile)
    
    driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/button[2]')\
        .click()

    time.sleep(2)

    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable\
        ((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable\
        ((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    username.send_keys(name)
    password.clear()
    password.send_keys(passw)
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable\
        ((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(5)
    alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable\
            ((By.XPATH, '//button[contains(text(), "Nie teraz")]'))).click()
    #alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    
    for j in range(50):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
    
    time.sleep(2)
    html = driver.page_source
    driver.close()
    return html


def save_photos(images, folderName):
    path = os.getcwd()
    path = os.path.join(path, folderName)

    os.mkdir(path)
    counter = 0
    for image in images:
        fileName = str(counter) + '.jpg'
        save_as = os.path.join(path, fileName)
        wget.download(image, save_as)
        print(f"Saved {fileName} in {path}.")
        counter += 1


def scrap(folderName, profile):
    html = open_web(profile)
    soup = BeautifulSoup(html, 'lxml')
    result = []
    images = soup.find_all('div', {'class':'_aagv'})

    for ii in images:
        result.append(ii.img['src'])

    save_photos(result, folderName)


if __name__=="__main__":
    print("-----------Instagram Downloader----------------")
    print("-----------------------------------------------")
    folderName = input(str("Folder name:"))
    profile = input("Profile link:")
    scrap(folderName, profile)
    print("-----------------------------------------------")


