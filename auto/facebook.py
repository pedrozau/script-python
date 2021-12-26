from selenium import webdriver 
import threading
import time
import random
class Facebook:

    driver = webdriver.Chrome('chromedriver.exe')
    user_name = "pedrozau28@gmail.com"
    user_pass = "pedropython"
    command = "alert('Facebook roboto ')"

    def __init__(self):
        pass
        
    
    

    def login(self):
        
       # self.driver.execute_script(self.command)
       # time.sleep(5)
        self.driver.get('https://free.facebook.com')
        user_email = self.driver.find_element_by_name('email') 
        user_password = self.driver.find_element_by_name('pass')
        user_login = self.driver.find_element_by_name('login') 
       
        
        # send to form 
        user_email.send_keys(self.user_name)
        user_password.send_keys(self.user_pass)
        user_login.submit()
        
        user_check = self.driver.find_element_by_class_name('s.bx.by.bz.ca')
        user_check.click()
        time.sleep(1)
        self.friends()
        #<input value="OK" type="submit" class="s bx by bz ca">
    
    def friends(self):
        amigo = self.driver.find_element_by_xpath('//*[@id="header"]/nav/a[6]').click()
        
        #class="q bn cr cs bp bm"
        #confir = self.driver.find_elment_by_xpath('//*[@id="root"]/div[2]').click()
        while True:
            confirm = self.driver.find_element_by_xpath('//*[@id="friends_center_main"]/div[1]/div[1]/table/tbody/tr/td[2]/div[2]/a[1]').click()
            confirm = self.driver.find_element_by_xpath('//*[@id="friends_center_main"]/div[1]/div[2]/table/tbody/tr/td[2]/div[2]/a[1]').click()

    def like(self):

        while True:
            likes = self.driver.find_element_by_xpath('//*[@id="like_112216677968974"]/a[2]').click()
            next_ = self.driver_find_element_by_xpath('//*[@id="root"]/div[1]/a').click()