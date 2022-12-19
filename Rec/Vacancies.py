import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class vacancies(unittest.TestCase):
    def setUp(self) :
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    def test_a_recruitment(self):
        #step 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        
        #view Vacancies
        browser.find_element(By.LINK_TEXT,"Recruitment").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT,"Vacancies").click()
        time.sleep(3)
        
        #edit Vacancies
        browser.find_element(By.XPATH,"(//button[@type='button'])[6]").click()
        time.sleep(5)
        browser.find_element(By.XPATH,"(//input)[2]").send_keys(Keys.CONTROL + "a")
        browser.find_element(By.XPATH,"(//input)[2]").send_keys(Keys.DELETE)
        browser.find_element(By.XPATH,"(//input)[2]").send_keys("Administration Project")
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,".oxd-select-text-input").send_keys(Keys.ARROW_DOWN)
        browser.find_element(By.CSS_SELECTOR,".oxd-select-text-input").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
        time.sleep(2)
        
        #Add Vacancies
        browser.find_element(By.LINK_TEXT,"Vacancies").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("AI Developer")
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        browser.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("Linda Jane Anderson")
        browser.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys(Keys.DOWN)
        browser.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys(Keys.ENTER)
        time.sleep(3)
        browser.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]").send_keys("1")
        time.sleep(2)
        browser.find_element(By.XPATH,"(//button[normalize-space()='Save'])[1]").click()
        time.sleep(2)

        #Deleted all
        browser.find_element(By.LINK_TEXT,"Vacancies").click()
        time.sleep(3)
        browser.find_element(By.CLASS_NAME,"oxd-checkbox-wrapper").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//button[normalize-space()='Delete Selected']").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//button[normalize-space()='Yes, Delete']").click()
        time.sleep(5)


if __name__ == "__main__": 
    unittest.main()
