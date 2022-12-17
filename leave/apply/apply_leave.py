import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class applyLeave(unittest.TestCase): 
    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #Apply Leave
    def test_apply_leave(self): 
        # steps
        browser = self.browser #buka web browser
        browser.maximize_window()
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(2) > div > div:nth-child(2) > input").send_keys("Admin") # isi nama by Full XPATH
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password by XPATH, #email tidak boleh sama
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol login by XPATH
        time.sleep(2)
        
        #Open page leave
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("2023-10-11")
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input").send_keys(Keys.BACK_SPACE)
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input").send_keys("2023-10-12")
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div[2]/textarea").send_keys("leave for medical check up")
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button").click()
        time.sleep(2)

        #validasi
        response_message = browser.find_element(By.XPATH,"//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[1]").text
        self.assertEqual(response_message, 'Success')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()