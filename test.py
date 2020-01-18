#coding: utf-8

from selenium import webdriver



#ChromeDriver로 접속, 자원 로딩시간 3초
driver = webdriver.Chrome('C:/Users/YYJ/Desktop/Project/Python/team/chromedriver.exe')
driver.implicitly_wait(3)


#웹페이지 불러오기
driver.get('https://www.foodsafetykorea.go.kr/portal/specialinfo/searchInfoProduct.do?menu_grp=MENU_NEW04&menu_no=2815')

driver.find_element_by_xpath("""//*[@id="contents"]/div[1]/div[1]/ul/li[2]/a""").click()

driver.find_element_by_xpath("""//*[@id="mode2"]/div[2]/div[1]/ul/li[2]/a""").click()

driver.find_element_by_xpath("""//*[@id="mode2"]/div[2]/div[2]/div[2]/ul/li[1]/span""").click()

driver.find_element_by_xpath("""//*[@id="mode2"]/div[3]/span""").click()

driver.implicitly_wait(10)
for index in range (1,10):
    driver.find_element_by_xpath("""//*[@id="tbody"]/tr["""+str(index)+"""]/td[5]/a""").click()

    driver.find_element_by_xpath("""/html/body/div[3]/div/a""").click()
    driver.implicitly_wait(3)