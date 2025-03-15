import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # ✅ Запуск без UI
        chrome_options.add_argument("--no-sandbox")  # ✅ Запуск в CI/CD
        chrome_options.add_argument("--disable-dev-shm-usage")  # ✅ Фикс ошибок памяти
        chrome_options.add_argument("--disable-gpu")  # ✅ Убираем GPU (ненужен в headless)
        chrome_options.add_argument("--remote-debugging-port=9222")  # ✅ Избегаем конфликта с другим процессом Chrome
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    #driver.close()
    driver.quit()

