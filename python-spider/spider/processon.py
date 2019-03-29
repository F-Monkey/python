'''
Created on Nov 20, 2018

@author: F-Monkey
'''
from spider import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Processon(driver):
    url = 'https://www.processon.com/diagraming/5b35985ee4b056f7f0b82671'

    def __init__(self):
        driver.__init__(self)
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.__login__()
    
    def __login__(self):
        email = self.find(By.XPATH, '//*[@id="login_email"]')
        password = self.find(By.XPATH, '//*[@id="login_password"]')
        login_btn = self.find(By.XPATH, '//*[@id="signin_btn"]')
        email.send_keys('291257658@qq.com')
        password.send_keys('tjfa546019')
        login_btn.click()
    
    def move(self):
        element = self.find(By.XPATH, '//*[@id="panel_basic"]/div[4]/canvas')
        action = ActionChains(self.browser)
        i = 1;
        while i < 20: 
            action.drag_and_drop_by_offset(element, i * 40, i * 42).perform()
            i += 1
            sleep(5)
        sleep(5000)


if __name__ == '__main__':
    p = Processon()
    p.move()
