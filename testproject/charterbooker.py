from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html"

driver.get(URL)
time.sleep(1)
# TC01 first page
guest_number = Select(driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select'))
guest_number.select_by_value('2')
time.sleep(0.2)
btn1 = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button')
btn1.click()
# TC01 second page
date = driver.find_element_by_name('bf_date')
date.send_keys('2021.09.21.')
time_of_day = Select(driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select'))
time_of_day.select_by_value('Morning')
time.sleep(0.2)
hours = Select(driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select'))
hours.select_by_value('5')
time.sleep(0.2)
btn2 = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button')
btn2.click()
# TC01 third page
full_name = driver.find_element_by_name('bf_fullname')
full_name.send_keys('Elek Teszt')
time.sleep(0.2)
email = driver.find_element_by_name('bf_email')
btn3 = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button')

# TC02 email validation
email.send_keys('alma')
time.sleep(2)
btn3.click()
time.sleep(2)


def validator():
    if driver.find_element_by_id('bf_email-error').text == 'PLEASE ENTER A VALID EMAIL ADDRESS.':
        email.clear()
        email.send_keys('alma@')
        time.sleep(2)
        btn3.click()
        if driver.find_element_by_id('bf_email-error').text == 'PLEASE ENTER A VALID EMAIL ADDRESS.':
            email.clear()
            email.send_keys('teszt.elek@tester.com')
            time.sleep(2)
            btn3.click()
        else:
            pass
    else:
        pass


validator()
time.sleep(2)
# answer page
# assert driver.find_element_by_xpath("//*[@id='booking-form']/h2").text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like " \
#             "lightning (Unless we're sailing or eating tacos!). "
# # Unable to locate element..cant find it with xpath, tagname, id..
driver.close()
