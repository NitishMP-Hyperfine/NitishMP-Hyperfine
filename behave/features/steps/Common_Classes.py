import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Locators import Locator

scanner_URL_8080 = "https://10.52.11.48:8080/"
scanner_URL_8888 = "https://10.52.11.48:8888/"
executable_path = "/Users/Nprashanth/PycharmLocalProjects/NitishMP-Hyperfine/behave/drivers/chromedriver"
screenshotdirectory = "//Users//Nprashanth//Downloads//RegressionTestScreenshots//"
gmailURL = "https://accounts.google.com/ServiceLogin?sacu=1&scc=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&osid=1&service=mail&ss=1&ltmpl=default&rm=false#identifier"
user_id = "hri"
user_pwd = "Systems123"
gmailtestusername = "hyperfine.regressiontest@gmail.com"
gmailtestpassword = "1Lovelucy"

class Commonclasses(object):

    def LogintoHyperfineURL8080(context):
        context.driver = webdriver.Chrome(executable_path)
        context.driver.get(scanner_URL_8080)  # change the scanner IP address here to choose scanner
        context.driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").click()  # click on advance
        time.sleep(2)
        context.driver.find_element_by_xpath("/html/body/div/div[3]/p[2]/a").click()  # click on prox
        time.sleep(5)
        context.driver.find_element(By.XPATH, Locator.username).send_keys(user_id)
        context.driver.find_element(By.XPATH, Locator.password).send_keys(user_pwd)
        context.driver.find_element(By.XPATH, Locator.SignInButton).click()
        time.sleep(5)

    def LogintoHyperfineURL8888(context):
        context.driver = webdriver.Chrome(executable_path)
        context.driver.get(scanner_URL_8888)  # change the scanner IP address here to choose scanner
        context.driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").click()  # click on advance
        time.sleep(2)
        context.driver.find_element_by_xpath("/html/body/div/div[3]/p[2]/a").click()  # click on prox
        time.sleep(5)
        context.driver.find_element(By.XPATH, Locator.username).send_keys(user_id)
        context.driver.find_element(By.XPATH, Locator.password).send_keys(user_pwd)
        context.driver.find_element(By.XPATH, Locator.SignInButton).click()
        time.sleep(5)

    def getscreenshot(context, pageName):
        directory = screenshotdirectory
        time_string = time.asctime().replace(":", "")
        page = pageName
        filename = directory + time_string + page + ".png"
        context.driver.save_screenshot(filename)
        context.driver.save_screenshot(filename)
        context.driver.quit()

    def verifyPACSMWLAlarmsPresent(context):
        context.driver.find_element(By.ID, Locator.AlarmsButton).click()
        time.sleep(2)
        try:
            context.driver.find_element(By.XPATH, Locator.NoMWLServerConnectionMessageAlarm).is_displayed()
            context.driver.find_element(By.XPATH, Locator.NoPACSServerConnectionMessageAlarm).is_displayed()
        except:
            context.driver.close()
            assert False, "Alarm not found"
        context.driver.close()

    def VerifyNoAlarms(context):
        context.driver.find_element(By.XPATH, Locator.AlarmsButton).click()
        time.sleep(5)
        context.driver.find_element(By.XPATH, Locator.AlarmMenu).is_displayed()
        assert True
        context.driver.close()

    def VerifyEmail (context):
        context.driver = webdriver.Chrome(executable_path)
        context.driver.get(gmailURL)
        time.sleep(3)
        context.driver.find_element(By.ID, Locator.Gmailusername).send_keys(gmailtestusername)
        time.sleep(2)
        context.driver.find_element(By.XPATH, Locator.GmailNext).click()
        time.sleep(2)
        context.driver.find_element(By.XPATH, Locator.GmailPassword).send_keys(gmailtestpassword)
        time.sleep(2)
        context.driver.find_element(By.XPATH, Locator.GmailNext).click()
        time.sleep(8)

        NewEmail = context.driver.find_element(By.XPATH, Locator.FirstGmail).get_attribute('email')
        if NewEmail == "lucy@hyperfine.io":
            assert True
            context.driver.close()
        else:
            assert False
            context.driver.close()

        context.driver.quit()