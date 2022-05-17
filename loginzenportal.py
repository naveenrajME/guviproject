from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


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
        

    # fetch the entire webpage using Selenium Automation
    def get_data(self,url):
        self.d.get(url)
        return(self.d.page_source)


s = login()
s.auto_login('naveenraj0705@gmail.com','Naveen@07') # passing the user name and Password


