#京东
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
#
# driver.get("http://www.jd.com")
#
# driver.maximize_window()
#
# driver.find_element(by=By.ID,value="key").send_keys("手机膜")
#
# driver.find_element("xpath","//*[@class='button']").click()
# time.sleep(1)
# driver.find_element("xpath",'//*[@id="J_goodsList"]/ul/li[2]/div/div[1]/a/img').click()
#
# time.sleep(5)
# nwh = driver.window_handles[-1]
# driver.switch_to.window(nwh)
# driver.find_element(by=By.ID,value="InitCartUrl").click()
# time.sleep(2)
# driver.find_element("xpath",'//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
# time.sleep(200)
# driver.quit()


#淘宝
#
# driver = webdriver.Chrome()
# driver.get("http://www.suning.com")
# driver.maximize_window()
# driver.find_element(by=By.ID,value="searchKeywords").send_keys("筋膜枪")
# time.sleep(3)
# driver.find_element("xpath","//*[@class='search-btn btn-new']").click()
# time.sleep(3)
# driver.find_element(by=By.ID,value="ssdsn_search_pro_baoguang-1-1-1_1_01:0071068900_12197172602-gg").click()
#
# time.sleep(5)
# nwh = driver.window_handles[-1]
# driver.switch_to.window(nwh)
# driver.find_element(by=By.ID,value="addCart").click()
# time.sleep(2)
# driver.quit()

# B站

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")
driver.maximize_window()
driver.find_element("xpath","//*[@autocomplete='off']").send_keys("原神")
time.sleep(3)
driver.find_element("xpath","//*[@id='nav_searchform']/div").click()

time.sleep(5)
nwh = driver.window_handles[1]
driver.switch_to.window(nwh)
driver.find_element("xpath","//*[@id='all-list']/div[1]/div[2]/ul[4]/li[7]/a").click()
time.sleep(20)
nwh1 = driver.window_handles[2]
driver.switch_to.window(nwh1)
driver.find_element("xpath","//*[@id='arc_toolbar_report']/div[1]/span[1]").click()
time.sleep(10)

driver.quit()






