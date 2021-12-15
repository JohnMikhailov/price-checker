from app.config import config
from enums import LoginAttrs

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def login(browser):
    # TODO close unpredictable popups
    browser.get(config.NIKE_SITE_URL)

    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.ID, value=LoginAttrs.ENTER_BUTTON_ID.value))

    enter_button = browser.find_element(By.ID, value=LoginAttrs.ENTER_BUTTON_ID.value)
    enter_button.click()

    wait.until(lambda p: p.find_element(By.ID, value=LoginAttrs.NIKE_LOGIN_ID))

    nike_login = browser.find_element(By.ID, value=LoginAttrs.NIKE_LOGIN_ID)
    nike_password = browser.find_element(By.ID, value=LoginAttrs.NIKE_PASSWORD_ID)

    nike_login.send_keys(config.NIKE_SITE_LOGIN)
    nike_password.send_keys(config.NIKE_SITE_PASSWORD)

    kip_me_logged_in = browser.find_element(By.NAME, value=LoginAttrs.KIP_ME_LOGGED_ID_CHECKBOX_NAME)

    is_selected = kip_me_logged_in.get_property('checked')
    if is_selected:
        kip_me_logged_in.click()

    submit_button = browser.find_element(By.ID, value=LoginAttrs.SUBMIT_BUTTON_ID)
    submit_button.click()
