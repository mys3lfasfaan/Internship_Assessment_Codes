import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver

data = pd.read_excel('D:\ProCoding\Internship INTERNSHALA\Input.xlsx')
url = data.URL.to_list()
url_id = data.URL_ID.to_list()

driver = webdriver.Chrome('chromedriver')

errorfileno = 0

for i, j in zip(url_id, url):
    driver.get(j)
    try:
        title = driver.find_element(By.CLASS_NAME, value='td-post-title')
        paragraphs = driver.find_element(By.CLASS_NAME, value="td-post-content")
    except Exception:
        errorfileno = i
        print(errorfileno)
    filename = '{}.txt'.format(i)
    try:
        string = title.text, "\n\n", paragraphs.text
        with open(filename, "w", encoding="utf-8") as file:
            file.writelines(string)
    except Exception:
        string = ""
        with open(filename, "w", encoding="utf-8") as file:
            file.writelines(string)
    file.close()
    time.sleep(2)
