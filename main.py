from selenium import webdriver
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pymysql


URL = "https://www.endclothing.com/kr/latest-products/new-this-week"
driver = webdriver.Chrome('chromedriver')
driver.get(url=URL)
