import unittest
import time
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeFormbuilder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_formbuilder_chrome(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get("https://form.123formbuilder.com/5012206")

        driver.implicitly_wait(3)

        print(driver.current_url)
        assert "Online Quiz" in driver.title
        print("Title of the website is -", driver.title + "  everything is fine")

        # API testing
        print("Online Quiz website ", requests.get("https://form.123formbuilder.com/5012206").status_code, "as status Code")
        code = requests.get("https://form.123formbuilder.com/5012206").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not OK")

       #Which of the following animals is not a mammal?
        driver.find_element(By.XPATH, '//*[@aria-labelledby="radio-000000080"]').click()

        # What is the longest river in the world?
        driver.find_element(By.XPATH, '//*[@aria-labelledby="radio-0000000a0"]').click()

        #Which of the following inventions occured in the 17th century?
        driver.find_element(By.XPATH, '//*[@aria-labelledby="checkbox-0000000c-0"]').click()

        #What name is given to the programs ran by a computer, as opposed to the hardware ?
        driver.find_element(By.XPATH, '//*[@aria-labelledby="checkbox-0000000e-0"]').click()

        #What food group has the highest level of protein?

        driver.find_element(By.XPATH, '//*[@aria-labelledby="radio-000000100"]').click()

        #Your Email
        driver.find_element(By.XPATH, '//*[@type="email"]').clear()
        driver.find_element(By.XPATH, '//*[@type="email"]').send_keys("estrella.24634@gmail.com")
        driver.find_element(By.XPATH, '//*[@class="normal-state"]').submit()

        assert "Online Quiz" in driver.title
        print("Page title in Chrome 1120x550 is:", driver.title)

        driver.quit()

        def tearDown(self):
            self.driver.quit()



class FirefoxFormbuilder(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox() # important

    def test_qasvus_chrome(self):
        driver = self.driver
        driver.set_window_size(1120, 850)
        driver.get("https://form.123formbuilder.com/5012206")

        driver.implicitly_wait(3)

        print(driver.current_url)
        assert "Online Quiz" in driver.title
        print("Title of the website is -", driver.title + "  everything is fine")

        # API testing
        print("Online Quiz website ", requests.get("https://form.123formbuilder.com/5012206").status_code,
              "as status Code")
        code = requests.get("https://form.123formbuilder.com/5012206").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not OK")

        # Which of the following animals is not a mammal?
        driver.find_element(By.XPATH, '//*[@aria-labelledby="radio-000000080"]').click()

        # What is the longest river in the world?
        driver.find_element(By.XPATH, '//*[@aria-labelledby="radio-0000000a0"]').click()

        # Which of the following inventions occured in the 17th century?
        driver.find_element(By.XPATH, '//*[@aria-labelledby="checkbox-0000000c-0"]').click()

        # What name is given to the programs ran by a computer, as opposed to the hardware ?
        driver.find_element(By.XPATH, '//*[@aria-labelledby="checkbox-0000000e-0"]').click()

        # What food group has the highest level of protein?

        driver.find_element(By.XPATH, '//*[@aria-labelledby="radio-000000100"]').click()

        # Your Email
        driver.find_element(By.XPATH, '//*[@type="email"]').clear()
        driver.find_element(By.XPATH, '//*[@type="email"]').send_keys("estrella.24634@gmail.com")
        driver.find_element(By.XPATH, '//*[@class="normal-state"]').submit()

        assert "Online Quiz" in driver.title
        print("Page title in .Firefox 1120x850 is:", driver.title)

        driver.quit()

        def tearDown(self):
            self.driver.quit()


