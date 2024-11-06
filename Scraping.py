from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

options = Options()
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
# options.add_argument(f'user-agent={user_agent}')
options.add_argument("--headless=new")

def Get_Info(driver, XPath):
    try:
        info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPath))).text
    except:
        info = 'NA'
    return info

def Scrape_YouLive(url_YL):
    driver = webdriver.Chrome(options=options)
    driver.get(url_YL)
    try:
        MLS =       Get_Info(driver, '/html/body/section[1]/section[6]/div[1]/div[1]/h3')
        price =     Get_Info(driver, '/html/body/section[1]/section[3]/div/div/span[1]/span[1]')
        size =      Get_Info(driver, '/html/body/section[1]/section[6]/div[4]/div[1]/span[2]')
        bed =       Get_Info(driver, '/html/body/section[1]/section[5]/div/div[2]/span[2]/span')
        bath =      Get_Info(driver, '/html/body/section[1]/section[5]/div/div[3]/span[2]/span')
        address =   Get_Info(driver, '/html/body/section[1]/section[4]/div[1]/div/h1')
        region =    Get_Info(driver, '/html/body/section[1]/section[4]/div[2]/div')
        building =  Get_Info(driver, '/html/body/section[1]/section[6]/div[7]/div/a')
        strata =    Get_Info(driver, '/html/body/section[1]/section[6]/div[5]/div[1]/span[2]')
        tax =       Get_Info(driver, '/html/body/section[1]/section[6]/div[5]/div[2]/span[2]')
        year =      Get_Info(driver, '/html/body/section[1]/section[6]/div[3]/div[2]/span[2]')
        assess =    Get_Info(driver, '/html/body/section[1]/section[9]/div[2]/div[1]/span[2]/span[1]/span')
        type =      Get_Info(driver, '/html/body/section[1]/section[5]/div/div[1]/span[2]/span')
        DOM =       Get_Info(driver, '/html/body/section[1]/section[6]/div[3]/div[1]/span[2]')
        amenities = Get_Info(driver, '/html/body/section[1]/section[6]/div[6]/div/span[2]')
        dict = {'MLS Code' : MLS, 'Link YouLive' : url_YL, 'Price' : price, 'Size' : size, 'Bedroom' : bed, 'Bathroom' : bath,
                'Address' : address, 'Region' : region, 'Building' : building, 'Strata' : strata, 'Tax' : tax, 'Year' : year,
                'Assessment' : assess, 'Type' : type, 'Day-on-Site' : DOM, 'Amenities' : amenities}
        df = pd.DataFrame([dict])
        print('House ', MLS, 'done')
    except:
        print('Error found on listing ', url_YL)
        dict = {'MLS Code': 'NA', 'Link YouLive': url_YL, 'Price': 'NA', 'Size': 'NA', 'Bedroom': 'NA', 'Bathroom': 'NA',
                'Address': 'NA', 'Region': 'NA', 'Building': 'NA', 'Strata': 'NA', 'Tax': 'NA', 'Year': 'NA',
                'Assessment': 'NA', 'Type': 'NA', 'Day-on-Site': 'NA', 'Amenities': 'NA'}
        df = pd.DataFrame([dict])
    finally:
        driver.quit()
    return df

# def Scrape_HouseSigma(url_HS):
#     driver = webdriver.Chrome(options=options)
#     driver.get(url_HS)
#     MLS = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div[2]/div/section[2]/section[2]/div[1]/div[1]/dl/div[1]/dd/span')
#     return