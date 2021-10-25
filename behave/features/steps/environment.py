from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave.fixture import use_fixture_by_tag


def before_all(context):
    context.driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'))
    context.scanner_ip = "10.52.11.115"
    context.user = "hri"
    context.password = "Hri1ucy"


def after_all(context):
    context.driver.quit()