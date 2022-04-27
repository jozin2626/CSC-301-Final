from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    init_driver()


def init_driver():
    driver = webdriver.Firefox(executable_path='geckodriver-v0.31.0-win64\geckodriver.exe')
    driver.get('https://store.steampowered.com')
    navigate_page()
    
    
def navigate_page():
    pass


if __name__ == '__main__':
    main()