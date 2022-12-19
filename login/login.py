import pytest
from _pytest import mark
from _pytest.mark.structures import Mark
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

Invalid =[
  ("Adminn","admin123"), #Username salah pass benar
  ("Admin","admin1233"), #Username benar pass salah
  ("Adminn","admin1233") #Username salah pass salah
]

Blank= [
  ("","admin123",'1'), #Username kosong pass terisi
  ("Admin","",'2'), #Username terisi pass kosong
  ("","",'3') #Username kosong pass kosong
]

@pytest.fixture
def setup():
  driver = webdriver.Chrome(options=options)
  driver.maximize_window()
  driver.get("https://opensource-demo.orangehrmlive.com/")
  driver.implicitly_wait(10)
  yield driver
  driver.quit()
  
def test_login_page(setup):
  time.sleep(2)
  assert setup.find_element(By.XPATH, "//h5[normalize-space()='Login']").text == "Login"

def test_login_success(setup):
  time.sleep(2)
  setup.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
  setup.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
  time.sleep(3)
  assert setup.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text == "Dashboard"

@pytest.mark.parametrize('user,pw',Invalid)
def test_login_failed(setup,user,pw):
  time.sleep(2)
  setup.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
  setup.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pw)
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
  time.sleep(3)
  assert setup.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text == "Invalid credentials"

@pytest.mark.parametrize('user,pw,no',Blank)
def test_login_blank(setup,user,pw,no):
  time.sleep(2)
  setup.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
  setup.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pw)
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
  time.sleep(3)
  iterasi = no
  #iterasi ke-1 dan ke-3
  if (iterasi == '1'):
    assert setup.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'])[1]").text == "Required" 
  elif (iterasi == 2):
    assert setup.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'])[2]").text == "Required"
  elif (iterasi ==3):
    assert setup.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'])[1]").text == "Required"
    assert setup.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'])[2]").text == "Required"