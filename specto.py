from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "specto.settings")
django.setup()
from sunghwan.models import *
from decouple import config


if __name__ == '__main__':
    SPECTO = config('SPECTO_URL')
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(5)
    driver.get(SPECTO)

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

    controllerGroup: dict = dict()
    controllerGroup[td[8].text] = td[9].text
    controllerGroup[td[13].text] = td[14].text
    DateTime = ControllerGroup(**controllerGroup)
    DateTime.save()

    cycleDataGroup: dict = dict()
    cycleDataGroup['DateTime'] = DateTime
    cycleDataGroup[td[23].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[24].text
    cycleDataGroup[td[28].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[29].text
    cycleDataGroup[td[33].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[34].text
    CycleDataGroup(**cycleDataGroup).save()

    birdsGroup: dict = dict()
    birdsGroup['DateTime'] = DateTime
    birdsGroup[td[43].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[44].text
    birdsGroup[td[48].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[49].text
    birdsGroup[td[53].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[54].text
    birdsGroup[td[58].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[59].text
    BirdsGroup(**birdsGroup).save()
    
    probesGroup: dict = dict()
    probesGroup['DateTime'] = DateTime
    for i in range(68, 184, 5):
        probesGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    ProbesGroup(**probesGroup).save()

    fanGroup: dict = dict()
    fanGroup['DateTime'] = DateTime
    for i in range(193, 339, 5):
        fanGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    FanGroup(**fanGroup).save()

    coolingGroup: dict = dict()
    coolingGroup['DateTime'] = DateTime
    for i in range(348, 369, 5):
        coolingGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    CoolingGroup(**coolingGroup).save()

    windowsGroup: dict = dict()
    windowsGroup['DateTime'] = DateTime
    for i in range(378, 484, 5):
        windowsGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    WindowsGroup(**windowsGroup).save()

    airUnit1Group: dict = dict()
    airUnit1Group['DateTime'] = DateTime
    for i in range(493, 504, 5):
        airUnit1Group[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    AirUnit1Group(**airUnit1Group).save()

    foodGroup: dict = dict()
    foodGroup['DateTime'] = DateTime
    for i in range(513, 524, 5):
        foodGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    FoodGroup(**foodGroup).save()

    chartsGroup: dict = dict()
    chartsGroup['DateTime'] = DateTime
    for i in range(533, 544, 5):
        chartsGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    ChartsGroup(**chartsGroup).save()

    coilsGroup: dict = dict()
    coilsGroup['DateTime'] = DateTime
    for i in range(553, 559, 5):
        coilsGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    CoilsGroup(**coilsGroup).save()

    silosGroup: dict = dict()
    silosGroup['DateTime'] = DateTime
    for i in range(568, 639, 5):
        silosGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    SilosGroup(**silosGroup).save()

    waterGroup: dict = dict()
    waterGroup['DateTime'] = DateTime
    for i in range(648, 664, 5):
        waterGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    WaterGroup(**waterGroup).save()

    eggsCollectionGroup: dict = dict()
    eggsCollectionGroup['DateTime'] = DateTime
    for i in range(673, 694, 5):
        eggsCollectionGroup[td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_")] = td[i+1].text
    EggsCollectionGroup(**eggsCollectionGroup).save()

    driver.quit()

    #for i,ele in enumerate(td):
    #    print("#####", i, td[i].text.replace(" ", "_").replace("'", "").replace(".", "").replace("/", "").replace("-", "").replace("__", "_"))
