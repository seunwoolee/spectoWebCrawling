from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "specto.settings")
django.setup()
from crawling.models import ControllerGroup


def controllerGroup(**kwargs):
    print('###')
    # print(kwargs)
    # print(kwargs.values())
    Date = kwargs.get('Date')
    Time = kwargs.get('Time')
    ControllerGroup.objects.create(
        Date=Date,
        Time=Time,
    )

    for Date, Time in kwargs.items():
        print(kwargs.items())
        ControllerGroup(Date=Date, Time=Time).save()


# def controllerGroup(**kwargs):
#     print('###')

if __name__ == '__main__':
    SPECTO = 'http://118.34.86.119:9092/Home/Index/'
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(5)
    driver.get(SPECTO)

    LOGIN_INFO = {
        'UserName': 'SPECTO',
        'Password': '123456'
    }

    driver.find_element_by_css_selector('table > tbody > tr:nth-child(5) > td:nth-child(1) > button').click()
    driver.find_element_by_css_selector('table > tbody > tr:nth-child(5) > td:nth-child(2) > button').click()
    driver.find_element_by_css_selector('table > tbody > tr:nth-child(5) > td:nth-child(3) > button').click()
    driver.find_element_by_css_selector('table > tbody > tr:nth-child(3) > td:nth-child(1) > button').click()
    driver.find_element_by_css_selector('table > tbody > tr:nth-child(3) > td:nth-child(2) > button').click()
    driver.find_element_by_css_selector('table > tbody > tr:nth-child(3) > td:nth-child(3) > button').click()

    driver.find_element_by_xpath('//*[@id="fieldset-content"]/fieldset/table/tbody/tr[1]/td[1]/button').click()
    driver.find_element_by_xpath('//*[@id="usersdiv"]/button[2]').click()
    driver.find_element_by_xpath('//*[@id="fieldset-content"]/fieldset/div/table/tbody/tr[7]/td[3]/button').click()

    driver.implicitly_wait(5)

    driver.get('http://118.34.86.119:9092/Data/Groups/')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(('className', 'standartTreeRow'))
    )
    driver.execute_script("document.getElementsByClassName('standartTreeRow')[4].click()")

    time.sleep(2)

    html = driver.execute_script("return document.getElementsByClassName('obj row20px')[0].innerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    td = soup.select("tbody tr td")
    # print(td[9].text)
    controllerGroup_dict = {}
    controllerGroup_dict[td[8].text] = td[9].text
    controllerGroup_dict[td[13].text] = td[14].text
    # print(controllerGroup_dict)

    controllerGroup(**controllerGroup_dict)


    # for i,ele in enumerate(td):
    #     print(i,td[i].text)
