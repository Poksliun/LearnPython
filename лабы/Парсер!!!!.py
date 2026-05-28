import time

from playwright.sync_api import sync_playwright

URL_SITE = "https://fc.kantiana.ru/"
LOGIN = "VVStepanenko@stud.kantiana.ru"
PASSWORD = "Xui34var"


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(f"Открытие сайта: {URL_SITE}")
        page.goto(URL_SITE)

        try:
            #print("Ожидание формы авторизации...")
            page.wait_for_selector('input[name="username"]', timeout=5000)

            #print("Ввод учетных данных...")
            page.fill('input[name="username"]', LOGIN)
            page.fill('input[name="password"]', PASSWORD)

            # print("Нажатие кнопки входа...")
            page.click('button[type="submit"]')

            # page.wait_for_selector('a[href="/gym/classes/signup/"]', timeout=10000)
            time.sleep(3)
            page.locator('a[href="/gym/classes/signup/"]').all()[1].click()

            print("Скрипт отработал.")

        except Exception as e:
            print(f"Ошибка выполнения: {e}")

        input("Нажмите Enter для закрытия браузера...")
        browser.close()


if __name__ == "__main__":
    test_login()