import pandas as pd

scraped_url_df = pd.read_excel('Condo_House_Scraping_North_Vancouver.xlsx')
scraped_url = set(scraped_url_df[scraped_url_df.columns[2]].values.tolist())
scraped_url_NA = scraped_url_df[scraped_url_df['Price'].isna()]


print('All', len(scraped_url))
print('NA', len(scraped_url_NA))
print(scraped_url_df['Price'][1:20])