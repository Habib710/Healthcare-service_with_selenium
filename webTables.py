from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0, 1000)")

table = driver.find_element(By.TAG_NAME,"table")
rows = table.find_elements(By.TAG_NAME,"tr")

target_value = "UI Testing"
found = False

for row in rows:
    cells = row.find_elements(By.TAG_NAME,"td")
    for cell in cells:
        if target_value == cell.text:
             found = True
             


print(found)



time.sleep(2)
driver.quit()