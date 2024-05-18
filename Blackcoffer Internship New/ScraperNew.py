import time
import pandas as pd

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import os

directory = "C:\\Users\\Asfaan Hussain\\Desktop\\INTERNSHALA\\Blackcoffer Internship 2\\TextFiles"

data = pd.read_excel("C:\\Users\\Asfaan Hussain\\Desktop\\INTERNSHALA\\Blackcoffer Internship 2\\Input.xlsx")
url = data.URL.to_list()
url_id = data.URL_ID.to_list()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

errorfileno = 0

for i, j in zip(url_id, url):
    driver.get(j)
    try:
        title = driver.find_element(By.CLASS_NAME, value='entry-title')
        paragraphs = driver.find_element(By.CLASS_NAME, value="td-post-content")
    except Exception:
        errorfileno = i
        print(errorfileno)
    filename = '{}.txt'.format(i)
    filepath = os.path.join(directory, filename)
    try:
        content = title.text, "\n\n", paragraphs.text
        with open(filepath, 'w', encoding = "utf-8") as file:
            file.writelines(content)
    except Exception:
        content = ""
        with open(filepath, 'w', encoding = "utf-8") as file:
            file.writelines(content)
    file.close()
    time.sleep(1)
