import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("https://suninjuly.github.io/selects1.html")

    # 2. Получаем числа и считаем сумму
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    result = num1 + num2

    # 3. Выбираем в выпадающем списке полученную сумму
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))

    # 4. Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    time.sleep(10)

finally:
    browser.quit()
    