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

    def test_04_quick_search(self):
        #driver = self.driver
        driver.find_element_by_xpath('//app-title-bar/div/div[2]/div[1]/div[2]/div').click()
        sleep(1)
        menu_list = ['PD', '온도', 'DGA', '차단기동작', 'OLTC', 'Bushing']
        for menu in menu_list:
            driver.find_element_by_link_text('%s' % menu).click()
            print('%s' % menu, 'Selected.')
            if (menu == 'PD'):
                driver.find_element_by_xpath("//app-attribute-form/div/div[5]/div/div/div[2]").click()
            else:
                pass
            driver.find_element(By.CSS_SELECTOR, ".attribute-selector").click()
            duration = ['Day', 'Week', 'Month']
            arrow = ['left', 'right']
            for d in duration:
                dropdown = driver.find_element(By.CSS_SELECTOR, ".attribute-selector")
                dropdown.find_element(By.XPATH, "//option[. = '%s']" % d).click()
                driver.find_element(By.CSS_SELECTOR, ".attribute-selector").click()
                #for a in arrow :
                    #driver.find_element_by_css_selector(".arrow-%s" % a).click()
                if (d == 'Day'):
                    driver.find_element_by_xpath("//app-time-line/div/div[2]/div[1]/div[25]")
                    try:
                        driver.find_element_by_xpath("//app-time-line/div/div[2]/div[1]/div[26]")
                    except selenium.common.exceptions.NoSuchElementException:
                        print("Day: Pass")
                elif (d == 'Week'):
                    driver.find_element_by_xpath("//app-time-line/div/div[2]/div[1]/div[8]")
                    try:
                        driver.find_element_by_xpath("//app-time-line/div/div[2]/div[1]/div[9]")
                    except selenium.common.exceptions.NoSuchElementException:
                        print("Week: Pass")
                elif (d == 'Month'):
                    driver.find_element_by_xpath("//app-time-line/div/div[2]/div[1]/div[31]")
                    try:
                        driver.find_element_by_xpath("//app-time-line/div/div[2]/div[1]/div[32]")
                    except selenium.common.exceptions.NoSuchElementException:
                        print("Month: Pass")
                else:
                    print("Wrong duration")

    #def tearDown(self):
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()