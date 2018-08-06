from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os

def register_class(username, password, section_index):
    
    #Make sure that the path to webdrivers is set in Windows Path Variable
    driver = webdriver.Chrome()

    driver.get("https://cas.rutgers.edu/login?service=https%3A%2F%2Fsims.rutgers.edu%2Fwebreg%2Fj_spring_cas_security_check")
    
    
    #login page
    username = driver.find_element_by_id('username').send_keys(username)
    password = driver.find_element_by_id('password').send_keys(password)
    login = driver.find_element_by_name('submit').click()

    
    #semester selection page
    semester = driver.find_element_by_id("semesterSelection3").click()
    submit_btn = driver.find_element_by_id("submit").click()

    #manage courses page
    input1 = driver.find_element_by_id("i1")
    input1.send_keys(section_index)
    driver.find_element_by_id("submit").click()

    #Transactions summary page
    success = driver.find_elements_by_class_name("ok")

    #check if successful and save screenshot
    driver.save_screenshot(os.path.abspath('screenshots/'+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.png'))
    if success:
        print("Course added successfully.")
        return True
    else:
        print("Error adding course. Go check screenshot.")
        return False
