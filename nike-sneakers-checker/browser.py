from selenium import webdriver
from app.config import config


chrome = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
