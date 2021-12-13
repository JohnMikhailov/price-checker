from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.config import config


def login(browser):
    browser.get(config.NIKE_SITE_URL)

    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.ID, value='top-nav-join-or-login-button'))
