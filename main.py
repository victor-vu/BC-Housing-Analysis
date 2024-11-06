import Filtering
import Scraping
import pandas as pd
import os

def Filter(url, file_name_export): ### Filtering all houses in a given area (from a given link)
    df = Filtering.Filter_YouLive(url)
    df.to_excel(file_name_export)

def Scrape(excelin, file_name_export): ### Scraping all houses found in a given excel file
    houses_url_df = pd.read_excel(excelin)
    houses_url = set(houses_url_df[houses_url_df.columns[1]].unique())
    df = pd.DataFrame()
    counter = 1
    for house_url in houses_url:
        print('Working on house number ', counter)
        df_house = Scraping.Scrape_YouLive(house_url)
        df = pd.concat([df, df_house])
        if counter % 30 == 0:
            df.to_excel('Tempo_' + file_name_export)
            print('Temporary data has been written to ', 'Tempo_' + file_name_export)
        counter = counter + 1
    df.to_excel(file_name_export)
    print('All data has been written to ', file_name_export)

def Scrape_Continue(excelin, excelout): ### To continue scraping if error happens, or to update a scraped data with new data
    houses_url_df = pd.read_excel(excelin)
    houses_url = set(houses_url_df[houses_url_df.columns[1]].unique())
    scraped_url_df = pd.read_excel(excelout)
    scraped_url = set(scraped_url_df[scraped_url_df.columns[2]].unique())
    scraped_url_NA = set(scraped_url_df[scraped_url_df['MLS Code'].isna()][scraped_url_df.columns[2]].unique())
    scraped_url_nonNA = scraped_url - scraped_url_NA
    houses_url = houses_url - scraped_url_nonNA
    df = pd.DataFrame()
    counter = 1
    for house_url in houses_url:
        print('Working on house number ', counter)
        df_house = Scraping.Scrape_YouLive(house_url)
        df = pd.concat([df, df_house])
        if counter % 30 == 0:
            df.to_excel('Tempo_' + 'Update_' + excelout)
            print('Temporary data has been written to ', 'Tempo_' + 'Update_' + excelout)
        counter = counter + 1
    file_name_export = 'Update_' + excelout
    df.to_excel(file_name_export)
    print('All data has been written to ', file_name_export)

if __name__ == '__main__':
    url = input('Input link from YouLive: ')
    area = input('Input area name: ')
    excel_for_filter = 'Condo_House_Filtering_' + area + '.xlsx'
    excel_for_scrape = 'Condo_House_Scraping_' + area + '.xlsx'
    if os.path.exists(excel_for_filter) == False:
        Filter(url, excel_for_filter)
    if os.path.exists(excel_for_scrape) == True:
        Scrape_Continue(excel_for_filter, excel_for_scrape)
    else:
        Scrape(excel_for_filter, excel_for_scrape)
