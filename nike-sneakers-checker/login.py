from app.config import config
from enums import LoginAttrs

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def get_log_in_inputs(browser):
    result = [
        e for e in browser.find_elements(By.TAG_NAME, value='input')
        if e.get_attribute('type') in ['email', 'password']
    ]

    e1, e2 = result

    if e1.get_attribute('type') == 'email':
        return e1, e2

    return e2, e1


def login(browser):
    # TODO close unpredictable popups
    browser.get(config.NIKE_SITE_URL)

    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.CLASS_NAME, value=LoginAttrs.ENTER_BUTTON_CLASS_NAME.value))

    enter_button = browser.find_element(By.CLASS_NAME, value=LoginAttrs.ENTER_BUTTON_CLASS_NAME.value)
    enter_button.click()

    wait.until(lambda p: p.find_element(By.ID, value=LoginAttrs.NIKE_ENTER_FORM_ID.value))

    nike_login, nike_password = get_log_in_inputs(browser)

    nike_login.send_keys(config.NIKE_SITE_LOGIN)
    nike_password.send_keys(config.NIKE_SITE_PASSWORD)

    keep_me_logged_in = browser.find_element(By.NAME, value=LoginAttrs.KEEP_ME_LOGGED_IN_CHECKBOX_NAME.value)

    is_clicked = keep_me_logged_in.get_property('checked')
    if is_clicked:
        keep_me_logged_in.click()

    submit_button = browser.find_element(By.CLASS_NAME, value=LoginAttrs.SUBMIT_BUTTON_CLASS_NAME.value)
    submit_button.click()
