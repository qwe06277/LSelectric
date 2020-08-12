# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest, time, re
from time import sleep

class CompactDauTestCase(unittest.TestCase):
    """
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\03.Util\chromedriver\chromedriver')
    """
    @classmethod
    def setUpClass(cls):
        global driver
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.maximize_window()
        #driver.implicitly_wait(5)
        driver.get('http://10.13.49.15:8080/ls_hmi')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "login-button")))
        """
        driver.find_element_by_xpath('//div[1]/input').send_keys('user')
        driver.find_element_by_xpath('//div[2]/input').send_keys('user')
        driver.find_elements_by_class_name('login-button')[0].click()
        """

    def test_01_pageloading(self):
        #driver = self.driver
        sleep(5)
        compact_dau_title = driver.title
        value = "LS HMI 0.1.6"
        self.assertEqual(value, compact_dau_title)

        #time.sleep(10)
        #driver.save_screenshot('compact_dau.png')
    
    def test_02_login(self):
        #driver = self.driver
        #driver.get('http://10.13.49.15:8080/ls_hmi')
        driver.find_element_by_xpath('//div[1]/input').send_keys('user')
        driver.find_element_by_xpath('//div[2]/input').send_keys('user')
        driver.find_elements_by_class_name('login-button')[0].click()

    def test_03_engineeringEuqipment(self):
        #engineering
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/div[1]/app-title-bar/div/div[2]/div[1]/div[7]/div').click()
        #전력설비
        driver.find_element_by_xpath("//a[contains(text(),'전력설비')]").click()
    
    def test_04_add_Site(self):
        try :
            #추가버튼클릭
            driver.find_element_by_xpath("/html/body/app-root/app-main/div/div[2]/div/app-new-tree/div/div[2]/app-new-logical-tree/div/div[1]/app-new-tree-search-form/div/div[2]/div[1]").click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"//app-new-tree-search-form/div/div[2]/div")))
            sleep(2)

            #이름입력
            driver.find_element_by_css_selector(".hideInputBox").send_keys('site')
            driver.find_element_by_css_selector(".hideInputBox").send_keys(Keys.ENTER)
            sleep(3)
            print("Success : site 추가")
        except :
            print("Fail : site 추가")
            pass

    def test_05_add_Building(self):
        try :
            #site선택
            driver.find_element_by_css_selector(".siteBox:nth-child(2) .clickBox").click()
            #추가버튼클릭
            driver.find_element_by_xpath("/html/body/app-root/app-main/div/div[2]/div/app-new-tree/div/div[2]/app-new-logical-tree/div/div[1]/app-new-tree-search-form/div/div[2]/div[1]").click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"//app-new-tree-search-form/div/div[2]/div")))
            sleep(2)
            #이름입력
            driver.find_element_by_css_selector(".hideInputBox").send_keys('Building')
            driver.find_element_by_css_selector(".hideInputBox").send_keys(Keys.ENTER)
            sleep(3)
            print("Success : Building 추가")
        except :
            print("Fail : Building 추가")
            pass


    def test_06_add_Room(self):
        try : 
            #Building선택
            driver.find_element_by_css_selector(".siteBox:nth-child(2) > .buildingBox .clickBox").click()
            #추가버튼클릭
            driver.find_element_by_xpath("/html/body/app-root/app-main/div/div[2]/div/app-new-tree/div/div[2]/app-new-logical-tree/div/div[1]/app-new-tree-search-form/div/div[2]/div[1]").click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"//app-new-tree-search-form/div/div[2]/div")))
            sleep(2)
            #이름입력
            driver.find_element_by_css_selector(".hideInputBox").send_keys('Room')
            driver.find_element_by_css_selector(".hideInputBox").send_keys(Keys.ENTER)
            sleep(3)
            print("Success : Room 추가")
        except :
            print("Fail : Room 추가")
            pass

    def test_07_add_Equipment(self):
        try :
            #Room선택
            driver.find_element_by_css_selector(".siteBox:nth-child(2) .roomBox .clickBox").click()
            #추가버튼클릭
            driver.find_element_by_xpath("/html/body/app-root/app-main/div/div[2]/div/app-new-tree/div/div[2]/app-new-logical-tree/div/div[1]/app-new-tree-search-form/div/div[2]/div[1]").click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,"//app-new-tree-search-form/div/div[2]/div")))
            sleep(2)
            #이름입력
            driver.find_element_by_css_selector(".hideInputBox").send_keys('Equipment')
            driver.find_element_by_css_selector(".hideInputBox").send_keys(Keys.ENTER)
            sleep(3)
            print("Success : Equipment 추가")
        except :
            print("Fail : Equipment 추가")
            pass

    def test_08_delete_Equipment(self):
        try : 
            #전력설비선택
            driver.find_element_by_css_selector(".siteBox:nth-child(2) > .buildingBox:nth-child(2) .panelBox .textContainer").click()
            #delete
            driver.find_element_by_xpath('//app-new-tree-search-form/div/div[2]/div[3]').click()
            #팝업 확인
            driver.find_element_by_css_selector(".whiteColorBlack").click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".whiteColorBlack")))
            sleep(3)
            print("Success : Equipment 삭제")
        except :
            print("Fail : Equipment 삭제")
            pass
    
    def test_09_delete_Room(self):
        try : 
            #Site
            driver.find_element_by_css_selector(".siteBox:nth-child(2) > .site > .icon").click()
            #Building
            driver.find_element_by_css_selector(".siteBox:nth-child(2) .building > .foldSimple").click()
            #Room
            driver.find_element_by_css_selector(".siteBox:nth-child(2) .roomBox .clickBox").click()
            #delete
            driver.find_element_by_xpath('//app-new-tree-search-form/div/div[2]/div[3]').click()
            #팝업 확인
            driver.find_element_by_css_selector(".whiteColorBlack").click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".whiteColorBlack")))
            
            sleep(3)
            print("Success : Room 삭제")
        except :
            print("Fail : Room 삭제")
            pass
    def test_10_delete_Building(self):
        try : 
            #Site
            driver.find_element_by_css_selector(".siteBox:nth-child(2) > .site > .icon").click()
            #Building
            driver.find_element_by_css_selector(".siteBox:nth-child(2) .building > .foldSimple").click()
            #delete
            driver.find_element_by_xpath('//app-new-tree-search-form/div/div[2]/div[3]').click()
            #팝업 확인
            driver.find_element_by_css_selector(".whiteColorBlack").click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".whiteColorBlack")))
            sleep(3)
            print("Success : Building 삭제")
        except :
            print("Fail : Building 삭제")
            pass

    def test_11_delete_Site(self):
        try : 
            #Site
            driver.find_element_by_css_selector(".siteBox:nth-child(2) > .site > .icon").click()
            #delete
            driver.find_element_by_xpath('//app-new-tree-search-form/div/div[2]/div[3]').click()
            #팝업 확인
            driver.find_element_by_css_selector(".whiteColorBlack").click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".whiteColorBlack")))
            sleep(3)
            print("Success : Site 삭제")
        except :
            print("Fail : Site 삭제")
            pass

    #def tearDown(self):
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()