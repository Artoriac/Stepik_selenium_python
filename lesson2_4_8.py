from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import math
import time
import re

def calc (x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button_book= browser.find_element(By.ID, "book").click()
    x_element = browser.find_element(By.ID, "input_value")
    x2_element = x_element.text
    y = calc(x2_element)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    submit_button = browser.find_element(By.ID, "solve").click()

    alert = browser.switch_to.alert
    print(alert.text)
    #text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)", alert_text)



finally:
    browser.close()
    browser.quit()