from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.config import config


def login(browser):
    # TODO close unpredictable popups
    browser.get(config.NIKE_SITE_URL)

    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(lambda p: p.find_element(By.ID, value='hf_title_signin_membership'))

    enter_button = browser.find_element(By.ID, value='hf_title_signin_membership')
    enter_button.click()

    nike_login = browser.find_element(By.ID, value='80ad225a-df94-4448-8e93-4681b0191b5f')
    nike_password = browser.find_element(By.ID, value='a9814734-3307-4253-8bf0-fd12951bb7f3')

    nike_login.send_keys(config.NIKE_SITE_LOGIN)
    nike_password.send_keys(config.NIKE_SITE_PASSWORD)

    kip_me_logged_in = browser.find_element(By.NAME, value='keepMeLoggedIn')

    is_selected = kip_me_logged_in.get_property('checked')
    if is_selected:
        kip_me_logged_in.click()

    submit_button = browser.find_element(By.ID, value='e589f9fd-c32a-4135-abcc-2a51b2138398')
    submit_button.click()
