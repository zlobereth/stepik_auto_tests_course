import math
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x: str) -> str:
    """Вычисляет ln(abs(12 * sin(x)))."""
    return str(math.log(abs(12 * math.sin(int(x)))))


def main():
    url = "http://suninjuly.github.io/explicit_wait2.html"

    driver = webdriver.Chrome()

    try:
        driver.get(url)

        # Ждем, пока цена станет ровно $100.
        # По условию ожидание должно быть не меньше 12 секунд.
        wait = WebDriverWait(driver, 12)
        wait.until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

        # Бронируем дом.
        driver.find_element(By.ID, "book").click()

        # Получаем x и решаем математическую задачу.
        x = driver.find_element(By.ID, "input_value").text
        answer = calc(x)

        driver.find_element(By.ID, "answer").send_keys(answer)
        driver.find_element(By.ID, "solve").click()

        # Получаем сообщение из alert и выводим код ответа в консоль.
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        message = alert.text

        print(message)

        match = re.search(r"\d+(?:\.\d+)?", message)
        if match:
            print(f"\nКод для ответа: {match.group(0)}")

        alert.accept()

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
