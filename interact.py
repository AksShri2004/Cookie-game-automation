from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_opt)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value='fName')
lname = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value="email")
# print(article_no.text)
list = [fname,lname,email]
def done(bruh):
    bruh.send_keys("AKSHAT_THE_GREAT@AksTG", Keys.ENTER)

for n in list:
    done(n)
# submit = driver.find_element(By.XPATH, value= '/html/body/form/button')
# submit.click()
# driver.quit()

