from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html"

driver.get(URL)
time.sleep(6)

# TC01 24 movies at first load
movies = driver.find_elements_by_xpath('//h2')
assert (len(movies)) == 24

# adding new movie
register = driver.find_element_by_class_name('mostra-container-cadastro')
register.click()
time.sleep(2)
title = driver.find_element_by_id('nomeFilme')
year = driver.find_element_by_id('anoLancamentoFilme')
order = driver.find_element_by_id('anoCronologiaFilme')
trailer = driver.find_element_by_id('linkTrailerFilme')
image = driver.find_element_by_id('linkImagemFilme')
summary = driver.find_element_by_id('linkImdbFilme')
title.send_keys('Black widow')
year.send_keys('2021')
order.send_keys('2020')
trailer.send_keys('https://www.youtube.com/watch?v=Fp9pNPdNwjI')
image.send_keys('https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg')
summary.send_keys('https://www.imdb.com/title/tt3480822/')
time.sleep(1)
save = driver.find_element_by_xpath('/html/body/div[2]/div[2]/fieldset/button[1]')
save.click()
time.sleep(2)

# TC2 checking new movie
movies = driver.find_elements_by_xpath('//h2')
assert (len(movies)) == 25

# Teszteld le, hogy fel lehet-e venni az alábbi adatokkal egy új filmet
# assert == 25 means new movie was added, does not mean however that it contains the correct details

driver.close()
