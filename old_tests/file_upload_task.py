from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "http://suninjuly.github.io/file_input.html"


def main():
    # Создаем пустой .txt файл рядом со скриптом.
    upload_file = Path(__file__).resolve().with_name("upload.txt")
    upload_file.touch(exist_ok=True)

    browser = webdriver.Chrome()

    try:
        browser.get(URL)

        # Заполняем имя, фамилию и email.
        browser.find_element(By.NAME, "firstname").send_keys("Ivan")
        browser.find_element(By.NAME, "lastname").send_keys("Petrov")
        browser.find_element(By.NAME, "email").send_keys("ivan.petrov@example.com")

        # Загружаем txt-файл.
        browser.find_element(By.ID, "file").send_keys(str(upload_file))

        # Отправляем форму.
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Получаем число из всплывающего окна.
        alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
        print("Ответ для задания:")
        print(alert.text)

        # Оставляем alert открытым, чтобы число можно было скопировать.
        input("\nНажмите Enter после того, как скопируете ответ...")
        alert.accept()

    finally:
        browser.quit()


if __name__ == "__main__":
    main()
