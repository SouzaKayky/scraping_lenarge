from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from utils.wait_and_click import wait_and_click
from time import sleep
import os

def download_table ():
    load_dotenv() 

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)  
    action = ActionChains(driver)

    url = os.getenv("URL_DRIVER")
    email = os.getenv("EMAIL_LENARGE")
    senha = os.getenv("SENHA_LENARGE")

    driver.get(url)
    
    inputs_login = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'input')))
    if len(inputs_login) >= 2:
        inputs_login[0].send_keys(email)
        inputs_login[1].send_keys(senha)
    else:
        raise Exception("Campos de login não encontrados!")
        
    wait_and_click(
        driver, "//button[@id='login-submit']"
            )
    wait_and_click(
        driver,
        '//a[span[contains(text(), "Operação")]]'
            )
    sleep(5)
    try: 
        driver.find_element(
            By.XPATH,
            '//span[@class="snack-action"]' 
                ).click() 
    except Exception as e:
        pass
    driver.find_element(
        By.XPATH,
        '//div[@role="rowgroup"]/div[@role="row"]//div[contains(@class, "control")]'
            ).click() 
 
    sleep(2)
    wait_and_click(
        driver, 
            '//button[contains(@class,"is-circle") and contains(@class,"is-primary")]'
            )
    wait_and_click(
        driver,
            '(//div[contains(@class, "h-select") and contains(@class, "has-loader")]//div[contains(@class, "select-box")][span[normalize-space(text())="Placas e Motorista"]])[1]'
            )
    wait_and_click(
        driver,
            '//div[@class="option-row"]/div[@class="option-meta"][span[normalize-space(text())="Completo"]]'
            )
    sleep(5)
    driver.find_element(
        By.XPATH,
        '//i[@class="far fa-file-excel"]'
        ).click()

    sleep(2)

