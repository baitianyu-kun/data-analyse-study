import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

service = Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=service, options=chrome_options)
for page_index in range(1, 30):
    driver.implicitly_wait(2)
    table = driver.find_element(By.CLASS_NAME, 'zg_table')
    table_items = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
    columns = table_items[0].find_elements(By.TAG_NAME, 'th')
    columns_row = []
    data_rows = []
    for column in columns:
        if column.text == '详情介绍':
            break
        columns_row.append(column.text)
    print("current_page:", page_index)
    for item in table_items:
        item_contents = item.find_elements(By.TAG_NAME, 'td')
        if len(item_contents) == 0:
            continue
        row = []
        for item_content in item_contents:
            if item_content.text == '职位详情':
                break
            row.append(item_content.text)
        data_rows.append(row)
    df = pd.DataFrame(data_rows, columns=columns_row)
    print(df)
    df.to_csv('./data.csv', mode='a', index=False, sep=',', encoding='utf_8_sig')

    next_pages_components = driver.find_element(By.CLASS_NAME, 'zg_page').find_element(By.TAG_NAME, 'p')
    next_pages_hrefs = next_pages_components.find_elements(By.TAG_NAME, 'a')
    for next_pages_href in next_pages_hrefs:
        if next_pages_href.text == '下一页':
            next_pages_href.click()
            break
