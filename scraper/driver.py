from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def get_driver():
    options = Options()
    options.set_preference("general.useragent.override",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    )
    
    service = Service(executable_path='D:\PycharmProjects\pythonProject\gecko driver\geckodriver.exe')

    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver