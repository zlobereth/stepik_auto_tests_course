from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("John")

    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Dow")

    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("johndow@test.gfd")

    # Заполняем необязательные поля
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    input4.send_keys("995003005060")

    input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    input5.send_keys("USA")

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Ждем загрузки страницы
    time.sleep(5)

    # Получаем текст результата
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Проверяем успешную регистрацию
    assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    # Ожидание для визуальной оценки результата
    time.sleep(5)

    # Закрываем браузер
    browser.quit()
    