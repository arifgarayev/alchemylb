import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BaseView:

    def __init__(self, driver):

        self.driver = driver

    def click(self, locator):

        "Returns self or raises TimeoutException"

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, locator))).click()
        return self

    def send_text(self, locator, text):

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, locator))).send_keys(text)
        return self


    def go_back(self):
        self.driver.back()

        return self


    def get_text(self, locator) -> str:

        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, locator))).text


    def check_app_state_view(self, locator) -> bool:

        time.sleep(5)

        try:

            self.driver.find_element_by_xpath(locator)

            time.sleep(3)

        except NoSuchElementException:

            return False

        return True



    def is_selected(self, locator):

        return self.driver.find_element_by_xpath(locator).is_selected()


    def wait_to_be_visible(self, locator):

        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, locator)))