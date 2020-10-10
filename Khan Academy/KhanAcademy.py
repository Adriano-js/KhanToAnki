import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request

chrome_options = webdriver.ChromeOptions()
option = webdriver.ChromeOptions()

chrome_prefs = {}

option.experimental_options["prefs"] = chrome_prefs

chrome_prefs["profile.default_content_settings"] = {"images": 2}

chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

driver = webdriver.Chrome(chrome_options=option)

links = ['https://pt.khanacademy.org/math/pt-4-ano', 'https://pt.khanacademy.org/math/pt-5-ano', 'https://pt.khanacademy.org/math/6-ano-matematica', 'https://pt.khanacademy.org/math/pt-7-ano', 'https://pt.khanacademy.org/math/pt-8-ano', 'https://pt.khanacademy.org/math/pt-9-ano', 'https://pt.khanacademy.org/math/math1', 'https://pt.khanacademy.org/math/math2', 'https://pt.khanacademy.org/math/math3']

x = 0
for link in links:
    print('//////////////////////////////////////////////////////////////////////////////////////////////')
    print('   ')
    driver.get(link)

    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#topic-progress > span > div > div > div._1fjpreec > div > nav > div._11dj4vig > ul > li:nth-child(2) > a > span._2970pgr')))

    elements = driver.find_elements_by_xpath('//*[@class="_dwmetq"]')

    for element in elements:
        materia = element.text

        if 'Desafio' in materia:
            continue

        if 'comunidade' in materia:
            continue

        try:
            separator = ':'
            materia = materia.split(separator, 1)[0]
        except:
            pass

        link = element.get_attribute('href')

        x += 1

        print(f'{x} | {materia} {link}')

        with open('KhanToAnki.txt') as f:
            f = open("KhanToAnki.txt", "a", encoding='utf-8')
            f.write(f'{x} | {materia} {link}')
            f.close()