from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def register_class(username, password):
    
    #Make sure that the path to webdrivers is set in Windows Path Variable
    driver = webdriver.Chrome()
    driver.get("https://cas.rutgers.edu/login?service=https%3A%2F%2Fsims.rutgers.edu%2Fwebreg%2Fj_spring_cas_security_check")
    
    username = driver.find_element_by_id('username').send_keys(username)
    password = driver.find_element_by_id('password').send_keys(password)
    time.sleep(10)