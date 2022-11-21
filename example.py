# selenium 4
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def setUpModule():
    print("setUpModule")

def tearDownModule():
    print("tearDownModule")

class TestRozetca(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.minimize_window()
        cls.driver.implicitly_wait(10);
        cls.driver.get("https://rozetka.com.ua/ua/")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")
        if cls.driver:
            cls.driver.quit()

    def test_login(self):
        btnProfile = self.driver.find_element(By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user/button")
        btnProfile.click()

        email = self.driver.find_element(By.XPATH,"//*[@id=\"auth_email\"]")
        email.send_keys("email")

        password = self.driver.find_element(By.XPATH,"//*[@id=\"auth_pass\"]")
        password.send_keys("pass")

        btnLogin = self.driver.find_element(By.XPATH,
            "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[1]");
        btnLogin.click()

        btnClPop = self.driver.find_element(By.XPATH,
            "/html/body/app-root/rz-single-modal-window/div[3]/div[1]/button")
        btnClPop.click()
        btnProfile.click()
        btnLogin.click()
