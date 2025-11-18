from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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


dropdown_element = driver.find_element(By.ID, "combo_facility")

select = Select(dropdown_element)

select.select_by_visible_text("Hongkong CURA Healthcare Center") 

driver.find_element(By.ID,"chk_hospotal_readmission").click()
driver.find_element(By.ID,"radio_program_medicaid").click()
driver.find_element(By.ID,"txt_visit_date").send_keys("30/12/2025")
driver.find_element(By.ID,"txt_comment").send_keys("Yes,I am done to test that")
driver.find_element(By.ID,"btn-book-appointment").click()
