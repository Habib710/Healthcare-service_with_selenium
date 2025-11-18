from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get("https://katalon-demo-cura.herokuapp.com/")

driver.maximize_window()
time.sleep(1)
driver.find_element(By.ID,"btn-make-appointment").click()



driver.find_element(By.ID,"txt-username").send_keys("John")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")

driver.find_element(By.ID,"btn-login").click()



time.sleep(1)

error_message = driver.find_element(By.CLASS_NAME, "text-danger").text

assert "Login failed! Please ensure the username and password are valid." in error_message

driver.find_element(By.ID,"txt-username").clear()
driver.find_element(By.ID,"txt-password").clear()


driver.find_element(By.ID,"txt-username").send_keys("John Doe")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNot")

driver.find_element(By.ID,"btn-login").click()
time.sleep(1)

error_message = driver.find_element(By.CLASS_NAME, "text-danger").text

assert "Login failed! Please ensure the username and password are valid." in error_message


driver.find_element(By.ID,"txt-username").clear()
driver.find_element(By.ID,"txt-password").clear()

driver.find_element(By.ID,"txt-username").send_keys("John Doe")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")

driver.find_element(By.ID,"btn-login").click()

driver.quit()