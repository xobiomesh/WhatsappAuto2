import os
import platform
from dotenv import load_dotenv

# Load environment variables from config.env file
def load_config():
    if platform.system() == "Windows":
        load_dotenv('config/config_windows.env')
    elif platform.system() == "Linux":
        load_dotenv('config/config_linux.env')
    else:
        print("Unsupported OS")
        exit(1)

def load_recipient_and_message():
    recipient_name = input("Enter the recipient's name: ")
    message = input("Enter the message: ")
    return recipient_name, message

import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    load_config()
    recipient_name, message = load_recipient_and_message()
    
    chromedriver_path = os.getenv('CHROMEDRIVER_PATH')
    chrome_binary_path = os.getenv('CHROME_BINARY_PATH')
    chrome_user_data_dir = os.getenv('CHROME_USER_DATA_DIR')

    # Debug prints to check if environment variables are loaded
    print(f"CHROMEDRIVER_PATH: {chromedriver_path}")
    print(f"CHROME_BINARY_PATH: {chrome_binary_path}")
    print(f"CHROME_USER_DATA_DIR: {chrome_user_data_dir}")

    if not chromedriver_path or not chrome_binary_path or not chrome_user_data_dir:
        logger.error("Environment variables for paths are not set.")
        return

    service = Service(chromedriver_path)
    
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_binary_path
    options.add_argument('--start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    # Specify the user data directory
    options.add_argument('user-data-dir={}'.format(chrome_user_data_dir))
    
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        
        driver.get('https://web.whatsapp.com')
        
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-tab="3"]'))
        )
        logger.info("Logged in successfully using the profile!")

        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        search_box.send_keys(recipient_name)
        search_box.send_keys(Keys.ENTER)

        chat_loaded = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//span[@title="{}"]'.format(recipient_name)))
        )
        chat_loaded.click()
        time.sleep(2)
        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
        )
        message_box.send_keys(message)
        time.sleep(2)
        send_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'))
        )
        time.sleep(2)
        send_button.click()

        logger.info("Message sent successfully!")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        raise

    finally:
        print("Closing the browser...")
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    main()
