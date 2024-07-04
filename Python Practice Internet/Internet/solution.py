from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class BrowserAutomation:
    def __init__(self, driver_path, headless=True):
        options = Options()
        options.headless = headless
        self.driver = webdriver.Chrome(service=Service(driver_path), options=options)

    def open_url(self, url):
        self.driver.get(url)
        time.sleep(2)

    def set_local_storage(self, key, value):
        script = f"window.localStorage.setItem('{key}', '{value}');"
        self.driver.execute_script(script)

    def get_local_storage(self, key):
        script = f"return window.localStorage.getItem('{key}');"
        value = self.driver.execute_script(script)
        return value

    def delete_local_storage(self, key):
        script = f"window.localStorage.removeItem('{key}');"
        self.driver.execute_script(script)

    def set_cookie(self, name, value):
        self.driver.add_cookie({'name': name, 'value': value})

    def get_cookie(self, name):
        cookie = self.driver.get_cookie(name)
        return cookie['value'] if cookie else None

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    driver_path = 'chromedriver'
    browser = BrowserAutomation(driver_path)

    # LocalStorage
    url = 'https://github.com'
    key = 'exampleKey'
    value = 'Hello world!'

    browser.open_url(url)
    browser.set_local_storage(key, value)
    print(f'Set LocalStorage: {key}={value}')
    stored_value = browser.get_local_storage(key)
    print(f"LocalStorage value: {stored_value}")
    browser.delete_local_storage(key)

    # Cookie
    browser.open_url(url)
    name = 'exampleCookieValue'
    value = '1234567890qwerty'

    browser.set_cookie(name, value)
    print(f'Set Cookie: {name}={value}')
    cookie_value = browser.get_cookie(name)
    print(f"Cookie value: {cookie_value}")
    browser.delete_cookie(name)

    browser.close()
