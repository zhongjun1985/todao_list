from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
import unittest
import HtmlTestRunner
import time
import os
import sys




class TestLink(unittest.TestCase):

    driver = webdriver.Chrome("E:\chromedriver_win32\chromedriver.exe")

    driver.maximize_window()

      
    def launch_webside(self):

        self.driver.get("https://todo-list-login.firebaseapp.com/")


    def Sign_in(self): 

        ## click github
        self.driver.find_element(By.XPATH, '/html/body/ng-view/div/a[4]').click()
        
        time.sleep(5)

        self.driver.switch_to.window(self.driver.window_handles[1])

        time.sleep(2)

        ## enter username   
        self.driver.find_element(By.XPATH, "//*[@id='login_field']").send_keys("username")

        ## enter password
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("password")

        self.driver.find_element(By.XPATH, "//*[@id='login']/div[3]/form/div/input[12]").click()

        self.driver.switch_to.window(self.driver.window_handles[0])

        time.sleep(5)

        ## verify login page
        Verify_todo_page = self.driver.find_element(By.XPATH, "/html/body/ng-view/div/div[1]")

        try:

            Verify_todo_page.text == "Todo Lists"

        except:

            print("Exception")


    def Enter_todo_list(self, text):
       
        time.sleep(1)

        ## enter to do list
        self.driver.find_element(By.XPATH, "/html/body/ng-view/div/div[2]/div[1]/input").send_keys(text)

        time.sleep(1)
        
        self.driver.find_element(By.XPATH, '/html/body/ng-view/div/div[2]/div[2]/button').click()

    
    def open_list(self, list_row):

        time.sleep(5)

        List_xpath = '/html/body/ng-view/div/div[3]/div/ul/li[{list_number}]/div/div[1]/a'

        list_xpath_row = List_xpath.replace("{list_number}", list_row)

        self.driver.find_element(By.XPATH, list_xpath_row).click()


    def add_tasks(self, tasks):

        self.driver.find_element(By.XPATH, "/html/body/ng-view/div/div[2]/div[1]/input").send_keys(tasks)

        self.driver.find_element(By.XPATH, "/html/body/ng-view/div/div[2]/div[2]/button").click()


    def delete_row_5_to_10(self,row_num):

        delete_button_xpath = '/html/body/ng-view/div/div[3]/div/ul/li[{row_number}]/div/div[2]/button'

        delete_button_xpath_row = delete_button_xpath.replace("{row_number}", row_num)

        self.driver.find_element(By.XPATH, delete_button_xpath_row).click()

    
    def test1(self):

        self.launch_webside()

        time.sleep(3)

        self.Sign_in()

        time.sleep(3)

        ## count the to do list after login
        orginal = self.driver.find_elements(By.XPATH, "//a[@class='ng-binding']")

        print("orginal: ", len(orginal))
        ## enter the to do list by list
        todo_list_input = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10']

        for i in range(len(todo_list_input)):

            self.Enter_todo_list(todo_list_input[i])

        time.sleep(3)    

        ## count the to do list after adding in
        after_add = self.driver.find_elements(By.XPATH, "//a[@class='ng-binding']")

        print("after add: ", len(after_add))

        ## verify the lists added correct
        self.assertTrue(len(orginal) == len(after_add) - 10)

        for a in range(1, len(after_add)):

            self.open_list(str(a))

            task_list = ["task1"]

            time.sleep(3) 

            for b in range(len(task_list)):

                self.add_tasks(task_list[b])

                time.sleep(3) 

                completed_checkbox = self.driver.find_elements(By.XPATH, "//button[@class='btn btn-info btn-block glyphicon glyphicon-unchecked ng-scope']")

                for checkbox in completed_checkbox:
            
                    checkbox.click()

                time.sleep(1)

                verify_task_completed =  self.driver.find_element(By.XPATH, "/html/body/ng-view/div/div[3]/div/div[2]")   

                self.assertTrue(verify_task_completed.text == "NaN/NaN Tasks Completed")

                time.sleep(2)

                self.driver.find_element(By.XPATH, "/html/body/ng-view/div/nav/div/div/a").click()

        ## Sign out
        self.driver.find_element(By.XPATH, "/html/body/ng-view/div/nav/div/ul/li/div/button").click()

        time.sleep(2)

        ## sign in via github again(dont know why but seems no need to enter the credential), anyway if this is not working, try sign in()
        ## self.Sign_in()
        self.driver.find_element(By.XPATH, '/html/body/ng-view/div/a[4]').click()

        time.sleep(8)

        ## delete the list 5-10 
        for r in range(5, 11):

            self.delete_row_5_to_10(str(r))

        after_delete = self.driver.find_elements(By.XPATH, "//a[@class='ng-binding']")

        print("after delete: ", len(after_delete))

        ## verify the list 5-10 delete
        self.assertTrue(len(after_add) == len(after_delete) + 6)

        time.sleep(2)
        ## sign out via github again
        self.driver.find_element(By.XPATH, '/html/body/ng-view/div/nav/div/ul/li/div/button').click()

        time.sleep(2)
        self.driver.quit()







        

