from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
'''Class to login in to the zenportal using usewrname and password'''
class login:
    d = webdriver.Firefox()
    '''Get in to the Zen Class portal and Login'''
    def auto_login(self,username, password):
       #Get the URL
        self.d.get('https://www.zenclass.in/')
        element=self.d.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input')
        element.send_keys(username)
        element=self.d.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input')
        element.send_keys(password) 
        element.send_keys(Keys.RETURN)
       
s = login()
s.auto_login('naveenraj0705@gmail.com','Naveen@07') # passing the user name and Password
