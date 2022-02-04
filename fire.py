import os
from random import randint
import time
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common import action_chains
from dotenv import load_dotenv
import pandas as pd


med = randint(3, 4)
short = 0.5


class Firefox:
    def __init__(self):

        global term
        term = f'marx'

    @staticmethod
    def driver_web(self):

        _ = f'driver_web{randint(1, 999)}'
        _ = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",
                              service_log_path="geckodriver.log",
                              firefox_profile="/home/studio/.mozilla/firefox/m5oe72jr.webdriver")

        _.set_window_size(950, 1070)

        return _


    @staticmethod
    def driver_safe(self):

        _ = f'driver_safe{randint(1, 999)}'
        _ = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",
                              service_log_path="geckodriver.log",
                              firefox_profile="/home/studio/.mozilla/firefox/f2jooh5d.safe")

        _.set_window_size(950, 1070)

        return _


    @staticmethod
    def driver_crude(self):

        _ = f'driver_safe{randint(1, 999)}'
        _ = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",
                              service_log_path="geckodriver.log",
                              firefox_profile="/home/studio/.mozilla/firefox/3ykqrr4i.crude")

        _.set_window_size(950, 1070)

        return _


    @staticmethod
    def driver_class(self):

        _ = f'driver_class{randint(1, 999)}'
        _ = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver",
                              service_log_path="geckodriver.log",
                              firefox_profile="/home/studio/.mozilla/firefox/2y5coacq.classroom")

        _.set_window_size(950, 1070)

        return _


    @staticmethod
    def timel():
        subprocess.run(["xterm", "-e", 'timeline', 'NEM.timeline'])


    @staticmethod
    def server_start():
        subprocess.run(["xterm", "-e", "python3", "ephor/manage.py", "migrate"])
        subprocess.run(["xterm", "-e", "python3", "ephor/manage.py", "makemigrations"])
        subprocess.run(["xterm", "-e", "python3", "ephor/manage.py", "runserver", "127.0.0.1:8000"])


    @staticmethod
    def twitter(_):
        _.get("https://twitter.com/home")
        start_time = time.time()
        date_Time_Obj = datetime.now()

        sleep(15)
        _.quit()

        timer = f'{date_Time_Obj}, Firefox - Twitter funcionou durante  {time.time() - start_time}'
        print(timer)


    @staticmethod
    def tweetdeck(_):
        _.get("https://tweetdeck.twitter.com/")
        start_time = time.time()
        date_Time_Obj = datetime.now()
    
        sleep(15)
        _.quit()

        timer = f'{date_Time_Obj} Firefox - Tweetdeck funcionou durante  {time.time() - start_time}'
        print(timer)


    @staticmethod
    def facebook(_):
        _.get("https://www.facebook.com/")
        start_time = time.time()
        date_Time_Obj = datetime.now()
    
        sleep(15)
        _.quit()

        timer = f'{date_Time_Obj} Firefox - Facebook funcionou durante  {time.time() - start_time}'
        print(timer)


    @staticmethod
    def instagram(_):
        _.get("https://www.instagram.com/")
        start_time = time.time()
        date_Time_Obj = datetime.now()
    
        sleep(15)
        _.quit()

        timer = f'{date_Time_Obj} Firefox - Instagram funcionou durante  {time.time() - start_time}'
        print(timer)


    @staticmethod
    def whatsapp(_):
        _.get("https://web.whatsapp.com/")
        start_time = time.time()
        date_Time_Obj = datetime.now()
    
        sleep(15)
        _.quit()

        timer = f'{date_Time_Obj} Firefox - Whatsapp funcionou durante  {time.time() - start_time}'


    @staticmethod
    def telegram(_):
        _.get("https://web.telegram.org/z/#-435704424")
        start_time = time.time()
        date_Time_Obj = datetime.now()
    
        sleep(15)
        _.quit()

        timer = f'{date_Time_Obj} Firefox - Telegram funcionou durante  {time.time() - start_time}'
        print(timer)


    @staticmethod
    def reddit(_):
        _.get("https://www.reddit.com/")
        start_time = time.time()
        date_Time_Obj = datetime.now()
    
        sleep(15)
        _.quit()

        timer = f'{date_Time_Obj} Firefox - Reddit funcionou durante  {time.time() - start_time}'
        print(timer)


    @staticmethod
    def news_google(_):
        _.get("https://news.google.com/topstories?hl=pt-BR&gl=BR&ceid=BR:pt-419")
        start_time = time.time()
        date_Time_Obj = datetime.now()
    
        sleep(15)
        _.quit()

        timer = f'{date_Time_Obj} Firefox - Google funcionou durante  {time.time() - start_time}'
        print(timer)


    @staticmethod
    def server_view(_):
        _.get("127.0.0.1:8000")

        sleep(15)
        _.quit()

        timer = f'{date_Time_Obj}, " Firefox funcionou durante  {time.time() - start_time}'
        print(timer)


    @staticmethod
    def acesso_change(_):

        router_info_00 = os.environ.get('RI01')
        router_info_01 = os.environ.get('RI02')
        load_dotenv()
        sleep(med)
        _.get("http://192.168.0.1/index.html")
        sleep(med)
        alfa = _.find_element(By.ID, "in_id")
        alfa.click()
        alfa.send_keys(router_info_00)
        beta = _.find_element(By.ID, "in_pw")
        beta.click()
        sleep(med)
        beta.send_keys(router_info_01)
        sleep(med)
        _.find_element(By.ID, "login-btn").click()
        sleep(med)
        _.find_element(By.LINK_TEXT, "Advanced Network Settings").click()
        sleep(med)
        _.find_element(By.LINK_TEXT, "Advanced").click()
        sleep(med)
        _.find_element(By.CSS_SELECTOR, '#sub-nav > li:nth-child(3) > a:nth-child(1)').click()
        sleep(med)
        _.find_element(By.CSS_SELECTOR, '#enable_5').click()
        sleep(med)
        _.find_element(By.CSS_SELECTOR, '.apply').click()
        sleep(med)
        _.find_element(By.CSS_SELECTOR, '#dialog3_confirmBtn').click()
        sleep(15)
        _.quit()

