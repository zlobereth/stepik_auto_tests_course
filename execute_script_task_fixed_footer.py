import math
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://suninjuly.github.io/execute_script.html"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 10)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def safe_click(element):
    """
    Элемент на этой странице может перекрываться огромным footer.
    Сначала перемещаем элемент в верхнюю часть viewport.
    Если обычный Selenium click всё равно перехватывается footer,
    выполняем клик через JavaScript.
    """
    browser.execute_script(
        """
        arguments[0].scrollIntoView({
            behavior: 'instant',
            block: 'start',
            inline: 'nearest'
        });
        window.scrollBy(0, -50);
        """,
        element,
    )

    try:
        element.click()
    except ElementClickInterceptedException:
        browser.execute_script("arguments[0].click();", element)


try:
    browser.get(URL)

    # Получаем значение x
    x = wait.until(
        EC.visibility_of_element_located((By.ID, "input_value"))
    ).text

    # Вычисляем функцию
    y = calc(x)

    # Вводим ответ
    answer = wait.until(
        EC.visibility_of_element_located((By.ID, "answer"))
    )
    answer.send_keys(y)

    # Checkbox "I'm the robot"
    robot_checkbox = wait.until(
        EC.presence_of_element_located((By.ID, "robotCheckbox"))
    )
    safe_click(robot_checkbox)

    # Radiobutton "Robots rule!"
    robots_rule = wait.until(
        EC.presence_of_element_located((By.ID, "robotsRule"))
    )
    safe_click(robots_rule)

    # Кнопка Submit
    submit_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn"))
    )
    safe_click(submit_button)

    # Получаем текст alert
    alert = wait.until(EC.alert_is_present())
    print("Ответ:", alert.text)

except Exception as error:
    print(f"{type(error).__name__}: {error}")

# browser.quit() специально не вызывается:
# благодаря detach=True окно Chrome останется открытым.
