import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoAlertPresentException,
    NoSuchWindowException,
    UnexpectedAlertPresentException,
)

URL = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return math.log(abs(12 * math.sin(x)))


driver = webdriver.Chrome()

try:
    # 1. Открываем исходную страницу
    driver.get(URL)

    # 2. Нажимаем кнопку
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 3. Сразу принимаем confirm
    driver.switch_to.alert.accept()

    # На следующей странице таймер всего 3 секунды,
    # поэтому никаких sleep() и долгих ожиданий здесь быть не должно.

    # 4. Получаем x, вычисляем ответ и вводим его
    x = float(driver.find_element(By.ID, "input_value").text)
    answer = calc(x)

    driver.find_element(By.ID, "answer").send_keys(str(answer))

    # 5. Отправляем форму
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 6. Сразу читаем итоговый alert
    result_alert = driver.switch_to.alert
    result_text = result_alert.text

    print("\nРезультат:")
    print(result_text)

    # Не держим alert открытым: сначала сохраняем текст, потом закрываем его.
    result_alert.accept()

    input("\nНажмите Enter, чтобы закрыть браузер...")

except NoSuchWindowException:
    print(
        "\nОшибка: окно было закрыто страницей по таймауту.\n"
        "На странице решения действует таймер около 3 секунд.\n"
        "Запустите скрипт ещё раз и не взаимодействуйте с браузером вручную."
    )

except NoAlertPresentException:
    print(
        "\nИтоговый alert не найден.\n"
        "Возможно, время истекло до отправки ответа или страница загрузилась некорректно."
    )

except UnexpectedAlertPresentException:
    # Если ChromeDriver сообщает об alert раньше, чем мы успели его получить,
    # пробуем прочитать его напрямую.
    try:
        alert = driver.switch_to.alert
        print("\nРезультат:")
        print(alert.text)
        alert.accept()
    except Exception as e:
        print(f"\nНе удалось прочитать alert: {e}")

finally:
    try:
        driver.quit()
    except Exception:
        pass
