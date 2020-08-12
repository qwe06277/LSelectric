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

    def test_03_engineeringDAU(self):
        #engineering
        driver.find_element_by_xpath('/html/body/app-root/app-main/div/div[1]/app-title-bar/div/div[2]/div[1]/div[7]/div').click()
        #DAU
        driver.find_element_by_xpath('//*[@id="main-content-container"]/app-engineering/div/div/div[1]/nav/div/a[3]')

    
    
    #testcase 1.19.10
    def test_04_connect(self):#왜안돼냐고;;;
        #DAU list
        #DAU_list = driver.find_elements_by_class_name("dauListNumber")[1]
        for i in range(1,5):
            #driver.find_element_by_css_selector("tr:nth-child(%s) > .dauListNumber:nth-child(3)"%i).click()
            driver.find_element_by_xpath('//*[@id="main-content-container"]/app-engineering/div/div/div[2]/app-dau-enginerring/div/div[1]/div/app-dau-list/div[2]/div/div/table/tbody/tr[%s]/td[3]'%i).click()
            #data.click()
            #Connect
            driver.find_element_by_css_selector(".connect-btn").click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".buttonContainer > .confirm")))
            driver.find_element_by_css_selector(".buttonContainer > .confirm").click()
            try :
                driver.find_element_by_css_selector(".buttonContainer > .popupBtn").click()
            except :
                print("button error")
                pass


    #testcase 1.19.11 Engineering_DAU - DAU로 부터 정보 읽기(SDDAU-V2) 수정 동작 테스트
    def test_05(self):
        #DAU등록
        driver.find_element_by_xpath('//*[@id="main-content-container"]/app-engineering/div/div/div[2]/app-dau-enginerring/div/div[1]/div/app-dau-list/div[2]/div/div/table/tbody/tr[1]/td[3]').click()
        #..아ㅏㅏㅏ않이 개빡

        
    #def tearDown(self):
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()