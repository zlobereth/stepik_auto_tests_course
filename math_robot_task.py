import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    # 1. Открыть страницу
    browser.get("https://suninjuly.github.io/get_attribute.html")

    # 2. Считать значение переменной x
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")

    # 3. Посчитать значение функции
    y = calc(x)

    # 4. Ввести ответ в текстовое поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # 5. Отметить checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # 6. Выбрать radiobutton "Robots rule!"
    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()

    # 7. Нажать Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Оставляем окно открытым на несколько секунд,
    # чтобы увидеть результат выполнения
    time.sleep(10)

finally:
    browser.quit()
