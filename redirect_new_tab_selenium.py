from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


URL = "http://suninjuly.github.io/redirect_accept.html"
TIMEOUT = 10


def calc(x: str) -> str:
    """Вычисляет значение функции из задания."""
    return str(log(abs(12 * sin(int(x)))))


def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, TIMEOUT)

    try:
        # 1. Открыть страницу
        driver.get(URL)

        # Запоминаем текущую вкладку
        original_window = driver.current_window_handle

        # 2. Нажать кнопку
        driver.find_element(By.CSS_SELECTOR, "button.trollface").click()

        # 3. Дождаться новой вкладки и переключиться на неё
        wait.until(lambda d: len(d.window_handles) > 1)

        new_window = next(
            handle for handle in driver.window_handles
            if handle != original_window
        )
        driver.switch_to.window(new_window)

        # 4. Получить x и решить капчу
        x = wait.until(
            lambda d: d.find_element(By.ID, "input_value").text
        )
        answer = calc(x)

        driver.find_element(By.ID, "answer").send_keys(answer)
        driver.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Получить число-ответ из alert
        alert = wait.until(lambda d: d.switch_to.alert)
        result_text = alert.text

        print("Сообщение:", result_text)

        # Из сообщения вида "Congrats, you've passed the task! Copy this code..."
        # можно вручную скопировать итоговое число из консоли.
        alert.accept()

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
