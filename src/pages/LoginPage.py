from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):  # this method is called when object of the class is created
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # implicity define time sleep

    def login_Button(self):   #THIS IS HOW FIND LOGIN PLACE
        try:
            login = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Login']"))
            )
            assert login.is_displayed(), "login input is not displayed on the page."
            login.click()

        except Exception as e:
            print(f"Assertion failed: {e}")

    def login_textbox(self):   #this is to send our login id to page
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='userid']"))
            )
            assert submit_button.is_displayed(), "login textbox is not displayed on the page."
            submit_button.send_keys(3004)


        except Exception as e:
            print(f"Assertion failed: {e}")

    def click_login(self):    #this one to click our login button to get in
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "// input[contains( @ value, 'Login')]"))
            )
            assert submit_button.is_displayed(), "log in button is not displayed on the page."
            submit_button.click()


        except Exception as e:
            print(f"Assertion failed: {e}")

    def click_logout(self):    #this one is to check logout button is working properly
        try:
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/logout']"))
            )
            assert logout_button.is_displayed(), "logout button is not displayed on the page."
            logout_button.click()


        except Exception as e:
            print(f"Assertion failed: {e}")

    def click_home(self):           #this one is click the home page after logout and to go find login button
        try:
            home_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Home']"))

            )
            assert home_button.is_displayed(), "Home button is not displayed on the page."
            home_button.click()


        except Exception as e:
            print(f"Assertion failed: {e}")

    def login_textbox2(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='userid']"))
            )
            assert submit_button.is_displayed(), "user id textbox is not displayed on the page."
            submit_button.send_keys(3004)



        except Exception as e:
            print(f"Assertion failed: {e}")

    def login_again(self):             #this one is login again after logout
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "// input[contains( @ value, 'Login')]"))
            )
            assert submit_button.is_displayed(), "log in button is not displayed on the page."
            submit_button.click()


        except Exception as e:
            print(f"Assertion failed: {e}")
