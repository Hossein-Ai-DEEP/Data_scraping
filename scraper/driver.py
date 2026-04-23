from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def get_driver():
    options = Options()
    # options.add_argument()
    
    service = Service(executable_path='D:\PycharmProjects\pythonProject\gecko driver\geckodriver.exe')

    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver