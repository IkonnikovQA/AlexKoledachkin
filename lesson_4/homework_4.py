from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://stepik.org/')
time.sleep(1)
title = driver.title
assert title == 'Каталог онлайн-курсов – Stepik'
time.sleep(1)
driver.get('https://ya.ru')
time.sleep(1)
title_ya = driver.title
assert title_ya == 'Яндекс'
time.sleep(1)
driver.back()
time.sleep(1)
assert title == 'Каталог онлайн-курсов – Stepik'
time.sleep(1)
driver.refresh()
time.sleep(1)
url = driver.current_url
assert url == 'https://stepik.org/catalog'
time.sleep(1)
driver.get('https://ya.ru')
time.sleep(1)
url_ya = driver.current_url
assert url_ya == 'https://ya.ru/'