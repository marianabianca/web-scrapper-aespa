from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote
import time
import datetime

op = webdriver.ChromeOptions()
op.add_argument('headless')

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')  # Update this path
# driver.get('https://www.ticketmaster.com.br/event/aespa')  # The URL of the SPA

def manda_mensagem_zap(driver):
    phone_no = "-"
    mensagem = quote("INGRESSO MEIA PREMIUM DISPONÍVEL CARAI CORRE https://www.ticketmaster.com.br/event/aespa")
    site = f"https://web.whatsapp.com/send?phone={phone_no}&text={mensagem}"
    driver.get(site)

    # Uses XPATH to find a send button
    element = lambda d : d.find_elements(by=By.XPATH, value="//div//button/span[@data-icon='send']")
    
    # Waits until send is found (in case of login)
    loaded = WebDriverWait(driver, 1000).until(method=element, message="User never signed in")
    
    # Loads a send button
    driver.implicitly_wait(10)
    send = element(driver)[0]
    
    # Clicks the send button
    send.click()
    
    # Sleeps for 5 secs to allow time for text to send before closing window
    time.sleep(5) 
    
    # Closes window
    driver.close()


def loga_zap(driver):
    site = f"https://web.whatsapp.com"
    driver.get(site)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[1]/div/span'))
    )


def remove_cookies_banner(driver):
    driver.get('https://www.ticketmaster.com.br/event/aespa')  # The URL of the SPA
    time.sleep(2)

    button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-reject-all-handler'))  # Update with your button's class
    )
    button.click()


def entra_ingressos(driver, contador=0):
    if contador > 5:
        print("deu errado visse")
        return
    try:
        time.sleep(5)

        button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'next'))  # Update with your button's class
        )
        button.click()

        time.sleep(5)
        
        button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'festival-selection'))  # Update with your button's class
        )
        button.click()
    except:
        driver.refresh()
        time.sleep(5)
        entra_ingressos(driver, (contador+1))




# Find the button and click it
try:
    loga_zap(driver)

    # Site do show
    remove_cookies_banner(driver)

    while True:
        entra_ingressos(driver)
        
        premium = driver.find_element(By.XPATH, "//h3[normalize-space()='Pista Premium']/parent::div")
        if (premium):
            meia = premium.find_element(By.XPATH, "//*[text()[(contains(.,'Meia-Entrada') and not(contains(.,'Idoso')))]]/parent::div/parent::div")

            # Check if "Meia-Entrada" is available
            if "not-available" in meia.get_attribute('class'):
                now = datetime.datetime.now()
                print("Meia-Entrada is not available.", f" {now.strftime('%d/%m - %H:%M:%S')}")
                driver.refresh()
            else:
                now = datetime.datetime.now()
                print("Meia-Entrada is available.", f" {now.strftime('%d/%m - %H:%M:%S')}")
                manda_mensagem_zap(driver)
                break
finally:
    driver.quit()






    


