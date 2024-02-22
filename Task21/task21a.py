from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Task:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            print("Cookies before login:")
            print(self.driver.get_cookies())

            return True
        except:
            print("ERROR : Unable to run the code !")
            return False

    def shutdown(self):
        self.driver.quit()

    def login(self):
        try:
            username_locator = "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input"
            password_locator = "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input"
            submit_button = "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input"

            self.driver.find_element(by=By.XPATH, value=username_locator).send_keys(self.username)
            print("Username filled")


            self.driver.find_element(by=By.XPATH, value=password_locator).send_keys(self.password)
            print("Password filled")
            self.driver.find_element(by=By.XPATH, value=submit_button).click()
            sleep(5)
            print("Submit Button clicked")
            print("Cookies after login:")
            print(self.driver.get_cookies())

        except NoSuchElementException as e:
            print("ERROR : Something went wrong with Locators !", e)


url = "https://www.saucedemo.com/"
username = "standarduser"
password = "secret_sauce"

execute = Task(url, username, password)

execute.booting_function()
execute.login()

execute.shutdown()
