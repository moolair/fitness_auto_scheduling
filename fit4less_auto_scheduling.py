import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import org.openqa.selenium.firefox.FirefoxDriver;
from datetime import date
import datetime


# Chrome
driver = webdriver.Chrome("C:/Python/Python38-32/Lib/site-packages/selenium/chromedriver_win32/chromedriver.exe")
# Firefox
#driver = webdriver.Firefox("C:/Python/Python38-32/Lib/site-packages/selenium/geckodriver.exe")
# Intenet explorer
#driver = webdriver.Ie("C:/Python/Python38-32/Lib/site-packages/selenium/chromedriver_win32/chromedriver.exe")

#username and pw
usernameStr = 'yjo8181@gmail.com'
passwordStr = '5iriet91'

wait = WebDriverWait(driver, timeout=1)
# Get into the website
driver.get("https://myfit4less.gymmanager.com/portal/login.asp")

# enter in the username and password
username = driver.find_element_by_id('emailaddress')
username.send_keys(usernameStr)
#password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
password = driver.find_element_by_id('password')
password.send_keys(passwordStr)

# sign in
signInButton = driver.find_element_by_id('loginButton')
signInButton.click()

#Select Day
selectDay = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'btn_date_select')))
selectDay.click()

# cancel today's 7am time at 8am (끝나기 30분전)
today = date.today()
todayDate = today.strftime('%A')
#print(todayDate)
theDayAfterTmr = date.today() + datetime.timedelta(days = 2)
#theDayAfterTmrDay = theDayAfterTmr.strftime('%A')
theDayAfterTmrDay = theDayAfterTmr.strftime('date_%Y-%m-%d')
#print(theDayAfterTmr)

# startDate = today.strftime("date_%Y-%m-%d")
#startDate = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-labelledby='modal_dates_Label']//*[contains(text(), 'Friday')]")))
startDate = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, theDayAfterTmrDay)))
startDate.click()

#Cancel process WHEN I need more sophisticate system********************
#cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-slotdate, 'Friday')]")))
# cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='reserved-slots']/div[@class='time-slot']//*[contains(text(), '7:00 AM')]/../.."))) 
# #book_5b78bc88-20b5-4f73-a516-e85c2d8c8efe
# #dialog_book_yes
# cancel.click()
# quit()

#Select date
if todayDate == 'Saturday' or todayDate == 'Sunday' or todayDate == 'Monday' or todayDate == 'Tuesday' or todayDate == 'Wednesday':
    selectDate = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='available-slots']//*[contains(text(), '7:00 AM')]/../..")))
else:
    pass
driver.execute_script("arguments[0].click();", selectDate)


#Reserve spot  
# reserveDate = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='available-slots']/div[@class='time-slot']//*[contains(text(), '7:00 PM')]/../..")))
# #time.sleep(2)
# #reserveDate = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'book_5b78bc88-20b5-4f73-a516-e85c2d8c8efe')))
# reserveDate.click()
dialogYes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'dialog_book_yes')))
dialogYes.click()




# dialog_cancel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, dialog_cancel_yes)))
# dialog_cancel.click()

# search for the day after tomorrow (if it's Saturday or Sunday, skip)

# click to book the time


"""
HowToMakeWebCrawler-With-Selenium저장된 페이지2017. 2. 26. - Selenium은 주로 웹앱을
테스트하는데 이용하는 프레임워크다. webdriver 라는 API를 통해 운영체제에 설치된 Chrome등의 브라우저를
제어하게 ...selenium 설치selenium javaselenium 버튼 클릭크롬 드라이버 64비트selenium xpath
사용법selenium headless함께 검색한 항목...
"""

# 검색 완료 후 크롬 창 최대화
#driver.maximize_window()
# 새로고침
driver.refresh()
# 3초 후 드라이버 종료(크롬창 닫힘)
time.sleep(1)
print('Test Completed')
driver.quit()
