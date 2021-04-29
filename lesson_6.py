from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    h = WebDriverWait(browser, 12).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.CSS_SELECTOR, "button#book").click()

    
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x)

    browser.find_element(By.CSS_SELECTOR, 'input#answer').send_keys(calc(x.text))

    browser.find_element(By.CSS_SELECTOR, "button#solve").click()

finally:
    # 10 секунд на ожидание
    time.sleep(10)
    # закрываем браузер после всех
    browser.quit()
# не забываем оставить пустую строку в конце файла
