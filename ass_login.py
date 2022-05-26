import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
'''Class to login in to the zenportal using usewrname and password'''
class login:
    d = webdriver.Firefox()
    '''Get in to the Zen Class portal and Login'''
    def auto_login(self,username, password):
       #Get the URL        
        self.d.get('https://www.zenclass.in/')
        # find the usename field
        element=self.d.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input')
        element.send_keys(username) # Fill the username in to the field
        #find the username field
        element=self.d.find_element(by=By.XPATH, value='//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input')
        element.send_keys(password) # fill the Password
        element.send_keys(Keys.RETURN) # Click the submit button
        time.sleep(5)
    '''Scrapping the co-ntents from the side menu'''
    def zen_menu_scrapping(self):
        # moving in to the side menu
        sidemenu = self.d.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/nav/ul')
        actions = ActionChains(self.d)
        actions.move_to_element(sidemenu).perform()
        # Get the side menu items
        export_content = sidemenu.text
        print(export_content)
        # write the Contents in to the documnet
        with open('assn1.txt', 'w') as a:
            a.write(export_content)
            a.close()           
s = login()
s.auto_login('naveenraj0705@gmail.com','Naveen@07') # passing the user name and Password
s.zen_menu_scrapping() 

