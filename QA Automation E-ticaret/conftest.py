import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config.config import BASE_URL


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    # Jenkins için headless çalışma
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Jenkins/Linux/CI uyumluluğu
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Popup ve kayıtlı şifre sorunlarını engelle
    options.add_argument("--incognito")
    options.add_argument("--disable-save-password-bubble")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()