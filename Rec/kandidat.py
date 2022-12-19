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
        #Login
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)

        #view candidates
        browser.find_element(By.LINK_TEXT,"Recruitment").click()
        time.sleep(2)
        browser.find_element(By.LINK_TEXT,"Candidates").click()
        time.sleep(5)



        #edit candidates
        browser.find_element(By.XPATH,"//div[11]//div[1]//div[7]//div[1]//button[1]//i[1]").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-left']").click()
        time.sleep(3)
        browser.find_element(By.NAME,"firstName").send_keys(Keys.CONTROL + "a")
        browser.find_element(By.NAME,"firstName").send_keys(Keys.DELETE)
        browser.find_element(By.NAME,"firstName").send_keys("Yudi")
        time.sleep(1)
        browser.find_element(By.NAME,"middleName").send_keys(Keys.CONTROL + "a")
        browser.find_element(By.NAME,"middleName").send_keys(Keys.DELETE)
        browser.find_element(By.NAME,"middleName").send_keys("Prasmeta")
        time.sleep(1)
        browser.find_element(By.NAME,"lastName").send_keys(Keys.CONTROL + "a")
        browser.find_element(By.NAME,"lastName").send_keys(Keys.DELETE)
        browser.find_element(By.NAME,"lastName").send_keys("Kewa")
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").send_keys(Keys.ARROW_DOWN)
        browser.find_element(By.CLASS_NAME,"oxd-select-text-input").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"(//input[@placeholder='Type here'])[1]").send_keys(Keys.CONTROL + "a")
        browser.find_element(By.XPATH,"(//input[@placeholder='Type here'])[1]").send_keys(Keys.DELETE)
        browser.find_element(By.XPATH,"(//input[@placeholder='Type here'])[1]").send_keys("yudikewa@pras.com")
        time.sleep(1)
        browser.find_element(By.XPATH,"(//input[@placeholder='Type here'])[2]").send_keys(Keys.CONTROL + "a")
        browser.find_element(By.XPATH,"(//input[@placeholder='Type here'])[2]").send_keys(Keys.DELETE)
        browser.find_element(By.XPATH,"(//input[@placeholder='Type here'])[2]").send_keys("12345")
        time.sleep(1)
        browser.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)




        #Validasi
        #response_data = browser.find_element(By.XPATH,"/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]").text
        #response_message = browser.find_element(By.CSS_SELECTOR,"/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text

if __name__ == "__main__": 
    unittest.main()
