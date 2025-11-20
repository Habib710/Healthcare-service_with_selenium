from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


driver = webdriver.Chrome()
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.switch_to.new_window()
driver.get("https://monkeytype.com/")
frist_tab = driver.window_handles[0]
driver.switch_to.window(frist_tab)
time.sleep(2)