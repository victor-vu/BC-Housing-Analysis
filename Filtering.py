from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

options = Options()
options.add_argument("--headless=new")

### Filtering building list from a given area in YouLive website
def Filter_Building_YouLive(url_YL):
    buildings_url = set()
    driver = webdriver.Chrome(options=options)
    driver.get(url_YL)
    try:
        buildings = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/section[2]/div/a')))
        for building in buildings:
            if building.get_attribute('class') == 'link-loading':
                buildings_url.add(building.get_attribute('href'))
    finally:
        driver.quit()
        print('URLs of ', len(buildings_url), 'buildings stored')
    return buildings_url

### Getting house list available on each building link
def Filter_House_YouLive(url_YL):
    houses_url = set()
    driver = webdriver.Chrome(options=options)
    driver.get(url_YL)
    try:
        houses = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/section[2]/div[2]/div/a')))
        for house in houses:
            if house.get_attribute('class') == 'link-loading':
                houses_url.add(house.get_attribute('href'))
    except:
        print('!!!!!!!!!! Error occurred. Manual entry required for ', url_YL)
    finally:
        driver.quit()
        print('URLs of ', len(houses_url), 'houses stored for', url_YL)
    return houses_url

def Filter_YouLive(url):
    buildings_url = Filter_Building_YouLive(url)
    houses_url = set()
    counter = 1
    for building_url in buildings_url:
        print('Working on building number ', counter)
        houses_url.update(Filter_House_YouLive(building_url))
        counter = counter + 1
    df = pd.DataFrame(list(houses_url))
    return df