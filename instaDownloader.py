from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import account


def openWeb():
    #dir to chromedriver
    s=Service("C:\ChromeDriver\chromedriver.exe")

    name = account.username()
    passw = account.password()


    #start windows maximized to allow scroll
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=s, options=options)
    #launch chrome with filmweb open
    driver.get('https://www.instagram.com/cats_of_instagram/')
    
    driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/button[2]').click()

    time.sleep(2)

    #target username
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    #enter username and password
    username.clear()
    username.send_keys(name)
    password.clear()
    password.send_keys(passw)

    #target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    time.sleep(5)
    alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Nie teraz")]'))).click()
    #alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    

    for j in range(20):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
    
    time.sleep(30)
    html = driver.page_source
    driver.close()
    return html



if __name__=="__main__":
    html = openWeb()

    soup = BeautifulSoup(html, 'lxml')

    result = []

    images = soup.find_all('div', {'class':'_aagv'})

    for i in images:
        result.append(i.img['src'])

    print(result)

