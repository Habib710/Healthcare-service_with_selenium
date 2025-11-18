from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get("https://katalon-demo-cura.herokuapp.com/")

driver.maximize_window()
time.sleep(1)
driver.find_element(By.ID,"btn-make-appointment").click()

# log in frsit.....

driver.find_element(By.ID,"txt-username").send_keys("John Doe")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")

driver.find_element(By.ID,"btn-login").click()

# book an apointment.................

