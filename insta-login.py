import time
import schedule

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def clock_work():
    web = webdriver.Chrome(ChromeDriverManager().install())
    web.get('https://www.instagram.com/')

    time.sleep(5)

    id_login = ""
    password = ""

    id_fill = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    id_fill.click()
    time.sleep(3)
    id_fill.send_keys(id_login)

    password_fill = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password_fill.click()
    time.sleep(3)
    password_fill.send_keys(password)

    time.sleep(3)
    enter_profile = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    enter_profile.click()

    time.sleep(5)
    refuse_save_info = web.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    refuse_save_info.click()


schedule.every().day.at("08:00:00").do(clock_work)


while 1:
    schedule.run_pending()
    time.sleep(1)
