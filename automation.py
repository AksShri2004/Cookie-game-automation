from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

start_time = time.time()
print(start_time)

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_opt)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def click_cookie():
    button = driver.find_element(By.CSS_SELECTOR, value="#cookie")
# for n in range (10000):
    button.click()


def get_value():
    money = int((driver.find_element(By.ID, value="money").text).replace(",",""))
    cursor_moni = re.findall(r"\d+", driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text)
    cursor_moni = "".join(cursor_moni)
    grandma_moni  = re.findall(r"\d+", driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b").text)
    grandma_moni = "".join(grandma_moni)
    factory_moni = re.findall(r"\d+", driver.find_element(By.CSS_SELECTOR, value="#buyFactory b").text)
    factory_moni = "".join(factory_moni)
    mine_moni = re.findall(r"\d+", driver.find_element(By.CSS_SELECTOR, value="#buyMine b").text)
    mine_moni = "".join(mine_moni)
    shipment_moni = re.findall(r"\d+", driver.find_element(By.CSS_SELECTOR, value="#buyShipment b").text)
    shipment_moni = "".join(shipment_moni)
    alchemy_moni = re.findall(r"\d+", driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text)
    alchemy_moni = ''.join(alchemy_moni)
    portal_moni = re.findall(r"\d+", driver.find_element(By.CSS_SELECTOR, value="#buyPortal b").text)
    portal_moni = "".join(portal_moni)
    timemachine_moni = re.findall(r"\d+", driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b').text)
    timemachine_moni = "".join(timemachine_moni)

    # key = ["cursor", "grandma", "factory", "mine", "shipment", "alchemy", "portal", "timemachine"]
    moni = {
        "buyCursor": int(cursor_moni),
        "buyGrandma":int(grandma_moni),
        "buyFactory":int(factory_moni ),
        "buyMine":int(mine_moni),
        "buyShipment":int(shipment_moni),
        "buyAlchemy lab":int(alchemy_moni),
        "buyPortal":int(portal_moni),
        "buyTime machine":int(timemachine_moni),
    }
    # print(moni)
    buy = ""
    for id_ in moni:
        if money >= int(moni[id_]):
            buy = id_



    # driver.find_element(By.ID, value=f"{buy}").click()
    try:
        driver.find_element(By.ID, value=buy).click()
        print(buy)
    except:
        pass


val = 0

while time.time() - start_time < 3000:
    click_cookie()
    time_ = int(time.time() - start_time)
    if time_ % 5 == 0 and time_ != val:
        get_value()
        val = time_