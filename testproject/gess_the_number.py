from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html"

driver.get(URL)
time.sleep(2)
# elements
number = driver.find_element_by_xpath('/html/body/div/div[2]/input')
guess = driver.find_element_by_xpath('/html/body/div/div[2]/span/button')
tries = driver.find_element_by_xpath('/html/body/div/div[3]/p/span')
result1 = driver.find_element_by_xpath('/html/body/div/p[3]')
result2 = driver.find_element_by_xpath('/html/body/div/p[4]')
result3 = driver.find_element_by_xpath('/html/body/div/p[5]')
reset = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/button')

# TC01 function to guess the number
'''
sehogy nem áll meg :(
valahogy számolni kellene hányszor fut le a ciklus, enumerate?
'''


def guesser():
    number.send_keys(101)
    guess.click()
    time.sleep(1)
    number.clear()
    if result1.text == "Guess lower." or result2.text == "Guess higher.":
        for i in (range(101)):
            number.send_keys(i)
            guess.click()
            time.sleep(0.1)
            number.clear()
    else:
        print(tries.text)


guesser()

# TC02
reset.click()
number.send_keys('-19')
guess.click()
assert result2.text == "Guess higher."
reset.click()
number.send_keys('255')
guess.click()
assert result1.text == "Guess lower."

driver.close()
