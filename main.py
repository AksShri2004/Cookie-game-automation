from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_opt)

# driver.get(url="https://www.amazon.in/MSI-Esports-Monitor-1920x1080-FreeSync/dp/B0BNGP36KY/?th=1")
#
# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(price)
#
# search = driver.find_element(By.NAME, value="field-keywords")
# print((search.size))
#
# instagram_link = driver.find_element(By.XPATH, value='//*[@id="navFooter"]/div[1]/div/div[3]/ul/li[3]/a')
# print(instagram_link.get_attribute("href"))
# driver.quit()

driver.get("https://www.python.org/")

elements = [n.text.split("\n") for n in driver.find_elements(By.CSS_SELECTOR, value='.event-widget li')]

df = pd.DataFrame(elements, columns=["DateTime", "EventName"])
df = df.to_dict("index")
# for n in elements:

print(df)


driver.quit()