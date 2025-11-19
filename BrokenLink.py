from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


driver = webdriver.Firefox()
driver.get("https://katalon-demo-cura.herokuapp.com/")

driver.maximize_window()

all_link = driver.find_elements(By.TAG_NAME,"a")
print(f"only find {len(all_link)} link in this page")
time.sleep(3)

for link in all_link:
    href = link.get_attribute("href")
    
    if href is None:
        print("Skipping link with no 'href' attribute.")
        continue 
        
    if href.startswith('javascript:') or href.startswith('mailto:'):
        print(f"Skipping non-HTTP link: {href}")
        continue
        
    
    try:
        respon = requests.get(href) 
        
        if respon.status_code >= 400:
            print(f"Broken link is: {href} (Status: {respon.status_code})")
        else:
             print(f"Good link: {href} (Status: {respon.status_code})") 
            
    except requests.exceptions.MissingSchema:
        print(f"Could not check link (Missing Schema, likely relative): {href}")
    except requests.exceptions.ConnectionError:
        print(f"Broken link (Connection Error): {href}")
    except Exception as e:
        
        print(f"Error checking link {href}: {e}")

driver.quit()