from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html"

driver.get(URL)
time.sleep(1)
# elements to list
periodic_table1 = driver.find_elements_by_xpath('//span')
periodic_table2 = []
for i in periodic_table1:
    periodic_table2.append(i.text)


# txt to list
with open('data.txt', 'r') as f:
    periodic_table3 = [line.strip() for line in f]

# assert the lists
assert periodic_table2 == periodic_table3

driver.close()

