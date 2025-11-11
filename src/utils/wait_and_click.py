
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def wait_and_click(driver, xpath, timeout=15):
    """
    Funcao dedicada ao web scraping da tabela no arquivo extract_table.
    """

    wait = WebDriverWait(driver, timeout)
    
    try:
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".infraloader.is-active")))
    except:
        pass  
    
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    
    driver.execute_script("arguments[0].click();", element)
    return element