from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
tar_get='https://www.express.com/clothing/women/striped-one-button-blazer/pro/06747392/color/Black%20and%20White%20Stripe/'

with open("douyin_cookie.pickle", 'rb') as file:
    cookies_list = pickle.load(file)
edge = webdriver.Edge()
edge.maximize_window()

    # 打开抖音网站
edge.get(tar_get)

    # 添加Cookie以实现持久登录
for cookie in cookies_list:
    edge.add_cookie(cookie)

edge.get(tar_get)
time.sleep(3)

wait=WebDriverWait(edge,10)
element=wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='bluecoreActionScreen']/div[6]/button")))
element.click()
# //*[@id="styliticsWidget"]/div/div/div[2]/div/div[4]
element=wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='styliticsWidget']/div/div/div[1]/div/div[2]")))
element.click()
time.sleep(300)