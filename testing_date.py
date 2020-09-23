import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import org.openqa.selenium.firefox.FirefoxDriver;
from datetime import date
import datetime

theDayAfterTmr = date.today() + datetime.timedelta(days = 2)
theDayAfterTmrDay = theDayAfterTmr.strftime('%A')
print(theDayAfterTmrDay)

time.sleep(3)