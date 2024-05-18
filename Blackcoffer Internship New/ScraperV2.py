# %%
import time
import pandas as pd

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import os

# %%
directory = "C:\\Users\\Asfaan Hussain\\Desktop\\INTERNSHALA\\Blackcoffer Internship New\\TextFiles"

data = pd.read_excel("C:\\Users\\Asfaan Hussain\\Desktop\\INTERNSHALA\\Blackcoffer Internship New\\Input.xlsx")
url = data.URL.to_list()
url_id = data.URL_ID.to_list()

# %%
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

# %%
error_file_no = 0
error_file_count = 0
error_file_list = []
error_file_url = []

for i, j in zip(url_id, url):
    driver.get(j)
    
    try:
        title = driver.find_element(By.XPATH, value="/html/body/div[6]/article/div[1]/div[1]/div[2]/div[2]/header/h1")
        paragraphs = driver.find_element(By.CLASS_NAME, value="td-post-content")
    except Exception:
        error_file_no = i
        error_file_count += 1
        error_file_list.append(error_file_no)
        error_file_url.append(j)
        
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



print(error_file_list)



for i,j in zip(error_file_list, error_file_url):
    driver.get(j)
    
    try:
        title = driver.find_element(By.XPATH, value="/html/body/div[6]/div[2]/div/div/article/div/div/div[2]/div/div[1]/div/div[4]/div/h1")
        paragraphs = driver.find_element(By.CLASS_NAME, value="td-post-content")
    except Exception:
        error_file_no = i
        error_file_count += 1
        print(error_file_no)
        
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
    time.sleep(0)

# %%
driver.close()


