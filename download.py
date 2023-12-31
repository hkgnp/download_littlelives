# import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

chrome_options = Options()
# Keep Chrome open
chrome_options.add_experimental_option("detach", True)


def download():
    # create instance of Chrome webdriver
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.littlelives.com/signin")

    driver.implicitly_wait(10)
    email = driver.find_element(by=By.NAME, value="email")
    email.send_keys("xx@xx.com")
    password = driver.find_element(by=By.NAME, value="password")
    password.send_keys("xx123xx123")
    button = driver.find_element(by=By.ID, value="btn-submit-sign-in")
    button.click()

    driver.implicitly_wait(20)

    x = 0
    while True:
        loadmore = driver.find_element(by=By.CLASS_NAME, value="loadmore-bottom")
        loadmore.click()
        time.sleep(0.5)
        x = x + 1
        if x == 75:
            break

    buttons = driver.find_elements(by=By.CLASS_NAME, value="download-all")

    for btn in buttons:
        ActionChains(driver).move_to_element(btn).perform()
        time.sleep(3)
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(3)


download()
