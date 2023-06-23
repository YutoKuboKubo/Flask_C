from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://news.yahoo.co.jp/topics/top-picks')

time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('p')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
# スクリーンショットの取得
driver.save_screenshot("screenshot.png")
driver.quit()

