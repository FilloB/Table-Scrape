from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import json
import time

URL = sys.argv[1]
n_players = int(sys.argv[2])

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    
    try:
        cookie_btn = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        cookie_btn.click()
    except:
        pass 
        
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bracket__name")))
    
    time.sleep(2)
    
    elements = driver.find_elements(By.CLASS_NAME, "bracket__name")
    
    players_formatted = []
    
    for el in elements:

        raw_text = el.get_attribute("textContent").strip()
        
        if raw_text.upper() == "BYE" or raw_text == "" or raw_text == "(Bye)":
            continue
            
        players_formatted.append(raw_text)
        
        if len(players_formatted) == n_players:
            break

    players_json = json.dumps(players_formatted, ensure_ascii=False)
    print(players_json)

finally:
    driver.quit()
