import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from Locators import Locator

kibanaURL = "https://hyperfine-staging.kb.us-east-1.aws.found.io/"
executable_path = "/Users/Nprashanth/PycharmLocalProjects/NitishMP-Hyperfine/behave/drivers/chromedriver"
screenshotdirectory = "//Users//Nprashanth//Downloads//RegressionTestScreenshots//"
userid_elasticseearch = "nprashanth"
pwd_elasticseearch = "Neethu_4148"
agenthostname: "agent.hostname:HG19480006"

class EventsPage(object):
    def VerifyMetadataEvents(context):
        context.driver.find_element(By.ID, Locator.EventsTab).click()
        time.sleep(3)
        event = context.driver.find_element(By.XPATH, Locator.MetadataEvent)
        if event.is_displayed():
            assert True
        else:
            assert False
        context.driver.quit()

    def VerifyHostEventsonKibana(context):
        context.driver = webdriver.Chrome(executable_path)
        context.driver.get(kibanaURL)
        time.sleep(5)
        context.driver.find_element(By.XPATH, Locator.LogintoElasticSearch).click()
        time.sleep(3)
        context.driver.find_element(By.XPATH, Locator.ElasticSearchUsrnme).send_keys(userid_elasticseearch)
        context.driver.find_element(By.XPATH, Locator.ElasticSearchPwd).send_keys(pwd_elasticseearch)
        context.driver.find_element(By.XPATH, Locator.ElasticSearchLoginButton).click()
        time.sleep(4)
        context.driver.find_element(By.XPATH, Locator.Kibana).click()
        time.sleep(4)
        context.driver.find_element(By.XPATH, Locator.DiscoverKibana).click()
        time.sleep(5)
        context.driver.find_element(By.XPATH, Locator.KibanaSearch).send_keys(agenthostname)
        context.driver.find_element(By.XPATH, Locator.RefreshButton).click()
        time.sleep(5)
        hostname = context.driver.find_element(By.XPATH, Locator.HostnameinTable)
        if hostname.is_displayed():
            assert True
            context.driver.quit()
        else:
            assert False
            context.driver.quit()
