import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver


df = pd.read_excel("C:/Users/Asfaan Hussain/Desktop/ABBU KE CHEZAN/LightBillAuto.xlsx")

site = "https://www.billdesk.com/pgidsk/pgmerc/tsspdclpgi/TSSPDCLPGIDetails.jsp"
driver = webdriver.Edge("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
driver.get("https://www.billdesk.com/pgidsk/pgmerc/tsspdclpgi/TSSPDCLPGIDetails.jsp")
