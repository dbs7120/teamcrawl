from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/dbs71/Desktop/파이썬/team/chromedriver.exe')
driver.implicitly_wait(3)


# 웹페이지 불러오기
driver.get('https://www.foodsafetykorea.go.kr/portal/specialinfo/searchInfoProduct.do?menu_grp=MENU_NEW04&menu_no=2815')
driver.find_element_by_xpath("""//*[@id="contents"]/div[1]/div[1]/ul/li[2]/a""").click()
driver.find_element_by_xpath("//*[@id='mode2']/div[2]/div[1]/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='mode2']/div[2]/div[2]/div[2]/ul/li[1]/span").click()
txt = driver.find_element_by_xpath("//*[@id='mode2']/div[3]/span").click()
driver.implicitly_wait(50)
time.sleep(3)

for page in range(3, 6):
    print(page-2, "쪽의 ")
    for i in range(1, 11):
        driver.implicitly_wait(50)
        driver.execute_script("window.open('');")
        time.sleep(3)
        print(i, "--> ")
        content = driver.find_element_by_css_selector('#tbody tr:nth-child(' + str(i) + ') td:nth-child(6) a')
        # WebElement 추출
        text = content.get_attribute('outerHTML')
        # 정수추출 정규식사용
        i = int(re.findall('\d+', text)[0])
        print(i)
        driver.switch_to.window(driver.window_handles[-1])
        driver.get('https://www.foodsafetykorea.go.kr/potalPopup/specialinfo/prdInfoDetail.do?prdlstReportLedgNo=' + str(i))
        time.sleep(3)
        driver.close()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(50)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    content = driver.find_element_by_css_selector('#contents > div.board-footer > div > ul > li:nth-child(' + str(page) +') > a')
    driver.execute_script("arguments[0].click();", content)
    driver.implicitly_wait(50)
driver.implicitly_wait(50)
