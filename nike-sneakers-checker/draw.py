from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.config import config
from excpetions import DrawError
from enums import DrawAttrs


def get_first_available_biggest_size(browser):
    all_list_items = browser.find_elements(By.TAG_NAME, value='li')
    sizes = sorted(
        (
            size for size in all_list_items
            if (config.NIKE_SNEAKERS_SIZE_PATTERN.upper() in size.text
                and size.get_attribute('data-qa') == DrawAttrs.DATA_QA_SIZE_AVAILABLE.value)
        ),
        key=lambda x: x.text,
        reverse=True
    )

    for size in sizes:
        if config.NIKE_SNEAKERS_DESIRED_SIZE in size.text:
            return size

    print('No desired size available')

    if sizes:
        return sizes[0]

    return sizes


def play(browser):
    wait = WebDriverWait(browser, timeout=config.MAX_WAIT_ELEMENT_APPEARANCE_SEC)
    wait.until(
        lambda p: p.find_element(
            By.CLASS_NAME,
            value='custom-link.ncss-label.fs14-sm.fs16-lg.mr5-sm.ml5-sm.ncss-brand.u-uppercase'
        )
    )
    browser.get(config.NIKE_SNEAKERS_FULL_URL)

    available_size = get_first_available_biggest_size(browser)
    if not available_size:
        raise DrawError('No available sizes')

    available_size.click()

    buy_button = browser.find_element(By.CLASS_NAME, value=DrawAttrs.BUY_BUTTON_CLASS_NAME.value)
    buy_button.click()
