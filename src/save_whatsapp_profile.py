import os
import platform
from dotenv import load_dotenv

def load_config():
    if platform.system() == "Windows":
        load_dotenv('../config/config_windows.env')
    elif platform.system() == "Linux":
        load_dotenv('../config/config_linux.env')
    else:
        print("Unsupported OS")
        exit(1)

import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_whatsapp_profile():
    load_config()
    
    chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
    chrome_binary_path = os.getenv('CHROME_BINARY_PATH')
    chrome_user_data_dir = os.getenv('CHROME_USER_DATA_DIR')

    if not chromedriver_path or not chrome_binary_path or not chrome_user_data_dir:
        logger.error("Environment variables for paths are not set.")
        return

    service = Service(chromedriver_path)
    
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_binary_path
    options.add_argument('--start-maximized')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('user-data-dir={}'.format(chrome_user_data_dir))
    
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get('https://web.whatsapp.com')
        
        # Wait for the QR code to be scanned and for WhatsApp to load
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-tab="3"]'))
        )
        logger.info("Logged in successfully using the profile!")
        time.sleep(5)  # Give some time to ensure profile is fully loaded

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
    finally:
        print("Closing the browser...")
        driver.quit()

if __name__ == "__main__":
    save_whatsapp_profile()
