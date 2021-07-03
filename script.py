from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import datetime
import time
import os
import keyboard

class meet_Bot:
    def __init__(self):
        self.bot = webdriver.Chrome("chromedriver.exe")

    def loginGmail(self, email, password):
        bot = self.bot
        bot.get(
            "https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        time.sleep(2)

        email_in = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        email_in.send_keys(email)
        time.sleep(2)

        buttom = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        buttom.click()
        time.sleep(2)

        password_in = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        password_in.send_keys(password)
        time.sleep(2)

        buttom = bot.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        buttom.click()
        time.sleep(2)

    def joinClassRoom(self, meet_Link):
        bot = self.bot
        bot.get(meet_Link)
        time.sleep(2)

        buttom = bot.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
        buttom.click()
        time.sleep(2)

        for i in range(3):
            keyboard.send("tab", do_press=True, do_release=True)
        keyboard.send("enter", do_press=True, do_release=True)
        time.sleep(2)

        for i in range(3):
            keyboard.send("tab", do_press=True, do_release=True)
        keyboard.send("enter", do_press=True, do_release=True)
        time.sleep(2)

        keyboard.send("control + e", do_press=True, do_release=True)
        time.sleep(2)

        enter_Reunion = bot.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span")
        enter_Reunion.click()





obj = meet_Bot()
obj.loginGmail("emial@ufms.br", "senha")

aulaED = "https://meet.google.com/qqd-rhrr-unh?pli=1&authuser=2"
obj.joinClassRoom(aulaED)



