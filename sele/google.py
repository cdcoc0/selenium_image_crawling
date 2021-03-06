from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("키티")
elem.send_keys(Keys.RETURN)
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for img in images:
    img.click()
    time.sleep(3)
    imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
    urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
    count += 1

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN): enter key
# assert "No results found." not in driver.page_source
# driver.close()