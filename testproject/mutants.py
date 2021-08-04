from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html"

driver.get(URL)
time.sleep(2)
# team filters
original_btn = driver.find_element_by_xpath('/html/body/div/label[1]')
force_btn = driver.find_element_by_xpath('/html/body/div/label[2]')
factor_btn = driver.find_element_by_xpath('//html/body/div/label[3]')
hellfire_btn = driver.find_element_by_xpath('//html/body/div/label[4]')

# members
all_members = driver.find_elements_by_xpath('//ul/li')
# original = []
# force = []
# factor = []
# hellfire = []

# which member belongs to which groups
# for i in range(16):
#     print(all_members[i].get_attribute("data-teams"))

# putting members to groups
''''
== nem jó mert van aki mind a 4 csoporthoz tartozik, olyan vizsgálat kellene, 
ami azt nézi hogy pl. "original" és bármi egyéb található ott, nem tudom van-e ilyen
mint pl SQLnél ha jól emlékszem $original$
'''
# def selector():
#     for i in range(16):
#         if all_members[i].get_attribute("data-teams") == original:
#             original.append(all_members[i].text)
#         elif all_members[i].get_attribute("data-teams") == force:
#             force.append(all_members[i].text)
#         elif all_members[i].get_attribute("data-teams") == factor:
#             factor.append(all_members[i].text)
#         else all_members[i].get_attribute("data-teams") == hellfire:
#             hellfire.append(all_members[i].text)


# print(original)
# print(force)
# print(factor)
# print(hellfire)


# trying to find a difference between members and non members
# angel = driver.find_element_by_id('angel')
# print(angel.text)
# emma_frost = driver.find_element_by_id('emma-frost')
# print(emma_frost.text)
# beast = driver.find_element_by_id('beast')
# print(beast.text)
# print(angel.value_of_css_property("opacity"))
# print(angel.value_of_css_property("transform"))
# print(angel.value_of_css_property("visibility"))
# print(emma_frost.value_of_css_property("opacity"))
# print(emma_frost.value_of_css_property("transform"))
# print(emma_frost.value_of_css_property("visibility"))
# hellfire.click()
# time.sleep(2)
# print(angel.text)
# print(emma_frost.text)
# print(beast.text)

# assert the difference between the groups
# hellfire_btn.click()
# for j in hellfire:
#     assert (driver.find_element_by_id(j).value_of_css_property("size")) == ('100x100')

driver.close()
