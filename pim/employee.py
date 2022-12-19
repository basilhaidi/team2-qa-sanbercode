import pytest
from _pytest import mark
from _pytest.mark.structures import Mark
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

@pytest.fixture
def setup():
  driver = webdriver.Chrome(options=options)
  driver.maximize_window()
  driver.get("https://opensource-demo.orangehrmlive.com/")
  driver.implicitly_wait(10)
  yield driver
  driver.quit()
  
def test_add_employee(setup):
  time.sleep(2)
  setup.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
  setup.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Basil")
  time.sleep(3)
  setup.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Haidi")
  time.sleep(3)
  setup.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Farizan")
  time.sleep(3)
  setup.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys(Keys.BACK_SPACE+ Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE + "BHF123")
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
  assert setup.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']").text == "Personal Details"

def test_add_employee_id_existing(setup):
  time.sleep(2)
  setup.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
  setup.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Max")
  time.sleep(3)
  setup.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Well")
  time.sleep(3)
  setup.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Fart")
  time.sleep(3)
  setup.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys(Keys.BACK_SPACE+ Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE + "BHF123")
  assert setup.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text == "Employee Id already exists"

def test_cancel_add_employee(setup):
  time.sleep(2)
  setup.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
  setup.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Robert")
  time.sleep(3)
  setup.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Cuy")
  time.sleep(3)
  setup.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Cunli")
  time.sleep(3)
  setup.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys(Keys.BACK_SPACE+ Keys.BACK_SPACE + Keys.BACK_SPACE + Keys.BACK_SPACE + "RCC123")
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
  time.sleep(3)
  assert setup.find_element(By.XPATH, "//a[normalize-space()='Employee List']").text == "Employee List"

def test_delete_employee(setup):
  time.sleep(2)
  setup.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
  setup.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "(//button[@type='button'])[4]").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Yes, Delete']").click()
  assert setup.find_element(By.XPATH, "//a[normalize-space()='Employee List']").text == "Employee List"

def test_cancel_delete_employee(setup):
  time.sleep(2)
  setup.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
  setup.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
  time.sleep(3)
  id_employee = setup.find_element(By.XPATH, "//div[normalize-space()='1998']").text() 
  setup.find_element(By.XPATH, "(//button[@type='button'])[4]").click()
  time.sleep(3)
  setup.find_element(By.XPATH, "//button[normalize-space()='No, Cancel']").click()
  assert setup.find_element(By.XPATH, "//a[normalize-space()='Employee List']").text == "Employee List"