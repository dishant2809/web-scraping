from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time


url = 'http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
driver.implicitly_wait(10)
driver.find_element_by_id('optlist_3').click()

drp = driver.find_element_by_id('ddlitem')

a=drp.text

a = list(a.split('\n'))


reg = []
for i in range(1,len(a)):
    reg.append(a[i])


drp = Select(drp)

for i in range(1,len(reg)+1):
    
    drp.select_by_index(i)
    
    driver.find_element_by_id('search').click()
    
    a = []
    while True:
        time.sleep(1)
        element = driver.find_element_by_xpath('//*[@id="Button1"]')
        
        a.append(driver.find_element_by_xpath('//*[@id="T1"]/tbody/tr/td').text)
        
        
        print(a)
        
        driver.execute_script("arguments[0].click();", element)


driver.maximize_window()
