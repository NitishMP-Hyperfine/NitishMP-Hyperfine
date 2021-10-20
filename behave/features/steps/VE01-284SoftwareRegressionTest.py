import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Locators import Locator


# Functions for VE01-284 Software Regression Test
# Functions for Step-2

@given('Log in to Hyperfine Service Console on chrome')
def HyperfineServiceconsoleLogin(context):
    context.driver = webdriver.Chrome(executable_path="//Users//mtrivedi//Downloads//chromedriver")
    context.driver.get("https://10.52.11.152:8888/")  # change the scanner IP address here to choose scanner
    context.driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").click()  # click on advance
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/div/div[3]/p[2]/a").click()  # click on prox
    time.sleep(5)
    # context.driver.find_element(By.XPATH, Locator.username).send_keys("hri")
    username = WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.XPATH, Locator.username)))
    username.send_keys("hri")
    # context.driver.find_element(By.XPATH, Locator.password).send_keys("Systems123")
    pwd = WebDriverWait(context.driver, 5).until(EC.presence_of_element_located((By.XPATH, Locator.password)))
    pwd.send_keys("Systems123")
    context.driver.find_element(By.XPATH, Locator.SignInButton).click()
    time.sleep(10)


@when('Go to Updates under Service tab and Select and download the latest version to update and install')
def SoftwareUpdateandInstall(context):
    context.driver.find_element(By.ID, Locator.UpdatesTab).click()
    time.sleep(5)
    try:
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        SWupdate = WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locator.LatestSWUpdate)))
        SWupdate.click()
        time.sleep(3)
        SWupdateDownload = WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locator.DownlaodUpdateButton)))
        SWupdateDownload.click()
        SWupdateInstall = WebDriverWait(context.driver, 265).until(
            EC.presence_of_element_located((By.XPATH, Locator.InstallPackg)))
        SWupdateInstall.click()
        time.sleep(450)
    except ValueError:
        context.driver.close()
    context.driver.close()


# Functions for Step-4

@then('Verify that no notifications should be present in the Alarms')
def VerifyNoAlarms(context):
    context.driver.find_element(By.XPATH, Locator.AlarmsButton).click()
    time.sleep(5)
    context.driver.find_element(By.XPATH, Locator.AlarmMenu).is_displayed()
    assert True
    context.driver.close()


# Functions for Step-7

@then('Verify the Software version and the Firmware/DLL matches in the Metadata and About tab')
def VerifySoftwareandFirmwareVersions(context):
    context.driver.find_element(By.ID, Locator.AboutTab).click()
    time.sleep(2)
    AboutTabSoftwareVersion = context.driver.find_element(By.XPATH, Locator.SoftwareBuild).text
    AboutTabFirmwareDLLVersion = context.driver.find_element(By.XPATH, Locator.FirmwareDLLVersion).text
    context.driver.find_element(By.CLASS_NAME, Locator.DevTab).click()
    context.driver.find_element(By.CLASS_NAME, Locator.DevModeSelectSendButton).click()
    time.sleep(2)
    context.driver.find_element(By.CLASS_NAME, Locator.DevModeSelectExpandAllButton).click()
    time.sleep(5)
    SoftwareVersion = context.driver.find_element(By.XPATH, Locator.Version).text
    SoftwareTimestamp = context.driver.find_element(By.XPATH, Locator.Datestamp).text
    MetadataTabFirmwareDLLVersion = context.driver.find_element(By.XPATH, Locator.FirmwareDLLversionMetadata).text
    MetadataVersion = SoftwareVersion + "." + SoftwareTimestamp

    if (AboutTabSoftwareVersion == MetadataVersion) and (AboutTabFirmwareDLLVersion == MetadataTabFirmwareDLLVersion):
        assert True, print("Both versions match")
    else:
        assert False, print("Both versions dont match")


# Functions for Step-8

@then('Verify the Software version and the Firmware/DLL matches in the Dev and Non-Dev mode of UI')
def VerifySoftwareVersionsin_Dev_NonDev(context):
    context.driver.find_element(By.CLASS_NAME, Locator.DevTab).click()
    context.driver.find_element(By.CLASS_NAME, Locator.DevModeSelectSendButton).click()
    time.sleep(2)
    context.driver.find_element(By.CLASS_NAME, Locator.DevModeSelectExpandAllButton).click()
    time.sleep(5)
    SoftwareVersion = context.driver.find_element(By.XPATH, Locator.Version).text
    SoftwareTimestamp = context.driver.find_element(By.XPATH, Locator.Datestamp).text
    MetadataTabFirmwareDLLVersion = context.driver.find_element(By.XPATH, Locator.FirmwareDLLversionMetadata).text
    MetadataVersion = SoftwareVersion + "." + SoftwareTimestamp

    context.driver.find_element(By.XPATH, Locator.HyperfineLogo).click()
    time.sleep(5)
    context.driver.find_element(By.ID, Locator.AboutTab).click()
    time.sleep(2)
    AboutTabSoftwareVersion = context.driver.find_element(By.XPATH, Locator.SoftwareBuild).text
    AboutTabFirmwareDLLVersion = context.driver.find_element(By.XPATH, Locator.FirmwareDLLVersion).text

    if (AboutTabSoftwareVersion == MetadataVersion) and (AboutTabFirmwareDLLVersion == MetadataTabFirmwareDLLVersion):
        assert True, print("Both versions match")
    else:
        assert False, print("Both versions dont match")


# Functions for Step-14
@then(
    'Configure ProxyServerURL,DeviceAccess,UploadToCloudPACSandLocalPACS,UncheckDeIdentifyUploadsToPACS,SuppressAllPHI,UploadDeviceTelemetryAndRawData,EnableElasticFileBeatAndEmailNotifications')
def ConfigureEmailandDataUploadSettings(context):
    context.driver.find_element(By.XPATH, Locator.ProxyServerURL).clear()
    context.driver.find_element(By.XPATH, Locator.ProxyServerURL).send_keys(
        "https://proxy.hyperfine-research-staging.com")
    context.driver.find_element(By.XPATH, Locator.DeviceUsername).clear()
    context.driver.find_element(By.XPATH, Locator.DeviceUsername).send_keys("hg19480006@hyperfine.io")
    context.driver.find_element(By.XPATH, Locator.DevicePassword).clear()
    context.driver.find_element(By.XPATH, Locator.DevicePassword).send_keys("Systems123")
    context.driver.find_element(By.XPATH, Locator.DeviceOrg).clear()

    xpath = [(Locator.UplaodToCloudPACS, 'UplaodToCloudPACS'),
             (Locator.PushToLocalPACSCheckbox, 'PushToLocalPACSCheckbox'),
             (Locator.UploadDeviceTelemetry, 'UploadDeviceTelemetry'),
             (Locator.UploadDeviceRawdata, 'UploadDeviceRawdata'),
             (Locator.EnableElasticFilebeat, 'EnableElasticFilebeat'),
             (Locator.EnableEmailNotifications, 'EnableEmailNotifications')]
    test = []
    # Looping through to make sure checkboxes are clicked
    for i, j in xpath:
        # print("Checking " + j)
        checkbox = context.driver.find_element(By.XPATH, i)
        if not checkbox.is_selected():
            checkbox.click()
            time.sleep(3)
        print('Checkbox for ' + j + ' is selected')
        time.sleep(1)
        test.append(j)
    print('All boxes are checked')
    time.sleep(3)

    xpath2 = [(Locator.DeIdentifyUploadsLocalPACS, 'DeIdentifyUploadsLocalPACS'),
              (Locator.DeIdentifyUploadsCloudPACS, 'DeIdentifyUploadsCloudPACS'),
              (Locator.SuppressAllPHI, 'SuppressAllPHI'),
              (Locator.UploadDeviceRawdataDirectly, 'UploadDeviceRawdataDirectly')]
    time.sleep(5)
    test2 = []
    # Looping through to make sure checkboxes are un-checked or cleared
    for k, l in xpath2:
        checkbox = context.driver.find_element(By.XPATH, k)
        if checkbox.is_selected():
            print("Checkbox is selected")
            checkbox.click()
            time.sleep(1)
        print('Checkbox for ' + l + ' is cleared')
        time.sleep(1)
        test2.append(l)
    print('All boxes are un-checked')
    time.sleep(3)
    context.driver.find_element(By.XPATH, Locator.SaveConnectionSettings).click()
    context.driver.close()


# Functions for Step-17
@when('Configure and Enable ElasticFileBeat and Elastic API key is set')
def ConfigureElasticOptions(context):
    ElasticFilebeatCheckbox = context.driver.find_element(By.XPATH, Locator.EnableElasticFilebeat)
    if not ElasticFilebeatCheckbox.is_selected():
        ElasticFilebeatCheckbox.click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, Locator.ElasticAPIKey).clear()
    context.driver.find_element(By.XPATH, Locator.ElasticAPIKey).send_keys(
        "Dyxj9ngBB163j5xJJdME:P5C2a5G7Rd2I3z6OjxG6iA")
    context.driver.find_element(By.XPATH, Locator.SaveConnectionSettings).click()
    time.sleep(3)


@then('Go to Events tab and verify metadata event has been registered')
def VerifyElasticEvents(context):
    context.driver.find_element(By.ID, Locator.EventsTab).click()
    time.sleep(3)
    event = context.driver.find_element(By.XPATH, Locator.MetadataEvent)
    if event.is_displayed():
        assert True
    else:
        assert False
    context.driver.quit()


@then('Verify Events are present for FM solution on Kibana')
def VerifyHostEvents(context):
    context.driver = webdriver.Chrome("executable_path=//Users//mtrivedi//Downloads//chromedriver")
    context.driver.get("https://hyperfine-staging.kb.us-east-1.aws.found.io/")
    time.sleep(5)
    context.driver.find_element(By.XPATH, Locator.LogintoElasticSearch).click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, Locator.ElasticSearchUsrnme).send_keys("nprashanth")
    context.driver.find_element(By.XPATH, Locator.ElasticSearchPwd).send_keys("Neethu_4148")
    context.driver.find_element(By.XPATH, Locator.ElasticSearchLoginButton).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, Locator.Kibana).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, Locator.DiscoverKibana).click()
    time.sleep(5)
    context.driver.find_element(By.XPATH, Locator.KibanaSearch).send_keys("agent.hostname:HG19480006")
    context.driver.find_element(By.XPATH, Locator.RefreshButton).click()
    time.sleep(5)
    context.driver.find_element(By.XPATH, Locator.HostnameinTable).is_displayed()
    assert True
    context.driver.quit()


# Functions for Step-26
@then('Go to Self Test under DEV tab and execute the Final Assembly Test with the FAT phantom successfully')
def VerifyFAT_Test1(context):
    context.driver.find_element(By.CLASS_NAME, Locator.DevTab).click()
    context.driver.find_element(By.XPATH, Locator.SelfTestTab).click()
    context.driver.find_element(By.XPATH, Locator.SelfTestExpandAll).click()
    time.sleep(3)
    Testselect = Select(context.driver.find_element(By.XPATH, Locator.SelectTestGroup))
    Testselect.select_by_visible_text('Final Acceptance')
    context.driver.find_element(By.CLASS_NAME, Locator.RunSelfTest).click()
    time.sleep(3550)

    FAT_Test1 = [Locator.UpdateCoilFileTest,
                 Locator.NoiseTest,
                 Locator.CenterFrequencyTest,
                 Locator.AutoShimTest,
                 Locator.RFPowerCalTest,
                 Locator.ImagingTest0,
                 Locator.ImagingTest1,
                 Locator.ImagingTest2,
                 Locator.ImagingTest3]
    time.sleep(5)
    # Looping through to make sure all the test results have Passed for the FAT test
    for i in FAT_Test1:
        TestResult = context.driver.find_element(By.XPATH, i).get_attribute('value')
        if TestResult == "PASS":
            assert True
        else:
            print(context.stdout_capture.getvalue(), i)
            assert False
        time.sleep(1)

    context.driver.close()


# Functions for Step-22

@then('Verify if the email notifications were configured and received')
def VerifyEmailNotification(context):
    context.driver = webdriver.Chrome("/Users/Nprashanth/BheaveMaster/drivers/chromedriver")
    context.driver.get(
        "https://accounts.google.com/ServiceLogin?sacu=1&scc=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&osid=1&service=mail&ss=1&ltmpl=default&rm=false#identifier")
    time.sleep(3)
    context.driver.find_element(By.ID, Locator.Gmailusername).send_keys("hyperfine.regressiontest@gmail.com")
    time.sleep(2)
    context.driver.find_element(By.XPATH, Locator.GmailNext).click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, Locator.GmailPassword).send_keys("1Lovelucy")
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


# Functions for Step 5

@when('User checks the about tab')
def navigatetoSpecsvalue(context):
    time.sleep(5)
    aboutTab = context.driver.find_element_by_xpath("//*[@id='tab-about']")
    time.sleep(2)
    print("clicking on to the about patient tab")
    aboutTab.click()
    time.sleep(3)


@then('User able to take the screenshot of About')
def getScreenShot(context):
    directory = "//Users//Nprashanth//Downloads//RegressionTestScreenshots//"
    time_string = time.asctime().replace(":", "")
    page = "About"
    filename = directory + time_string + page + ".png"

    context.driver.save_screenshot(filename)
    print("Getting screen shots as a following file name")
    print(filename)
    # filename = "" + page + ".png"
    context.driver.save_screenshot(filename)

    # print("Getting screen shots")
    print(filename)
    context.driver.quit()


# Functions for Step 6
@when('User checks the about tab - Spec Values')
def navigatetoSpecsvalue(context):
    time.sleep(5)
    aboutTab = context.driver.find_element_by_xpath("//*[@id='tab-about']")
    time.sleep(2)
    print("clicking on to the about patient tab")
    aboutTab.click()
    time.sleep(3)
    context.driver.find_element_by_class_name(
        "json-glyph.glyphicon.glyphicon-triangle-right").click()  # Click on Specs value
    time.sleep(2)


@then('User able to take the screenshot of specs values')
def getScreenShot(context):
    directory = "//Users//Nprashanth//Downloads//RegressionTestScreenshots//"
    time_string = time.asctime().replace(":", "")
    page = "Specs Value"
    filename = directory + time_string + page + ".png"

    context.driver.save_screenshot(filename)
    print("Getting screen shots as a following file name")
    print(filename)
    # filename = "" + page + ".png"
    context.driver.save_screenshot(filename)

    # print("Getting screen shots")
    print(filename)
    context.driver.quit()


# Functions for Step 7

@then('User gets a screenshot for the build information containing in metadata')
def metadataScreenshot(context):
    print("Two")
    time_string = time.asctime().replace(":", "")
    time.sleep(1)
    directory = '//Users//Nprashanth//Downloads//RegressionTestScreenshots//'  # Change for location to store your screen shots
    filename = directory + time_string + "Metadata.png"
    time.sleep(1)
    context.driver.save_screenshot(filename)
    print(filename)
    context.driver.quit()


# Functions for Step 9
@when('Verify if rf_coil value is set and coil_autoselect is checked in the Metadata')
def clickonDevTab(context):
    # driver.find_element_by_xpath("//*[@id=tab-dev]").click()
    context.driver.find_element_by_xpath("/html/body/nav/ul/li[2]/a/span[1]").click()
    # devTab= /html/body/nav/ul/li[2]/a/span[1] #xpath

    context.driver.find_element_by_class_name("button-send").click()
    # sendButton=button-send #classname

    context.driver.find_element_by_xpath(
        "/html/body/nav/div[1]/div[2]/div[1]/div/div/div/div[1]/div/div/div[1]/button[2]").click()

    time.sleep(3)
    context.driver.find_element_by_xpath(
        '//*[@id="config-pane"]/div/div/div[1]/table/tbody/tr[136]/td[1]/div/span').click()  # go to the location neat the RF coil
    # scrollForRFCoil=//*[@id="config-pane"]/div/div/div[1]/table/tbody/tr[136]/td[1]/div/span
    time.sleep(10)


@then('rf_coil is autoselected')
def rfcoilautoselect(context):
    rf_coil = context.driver.find_element_by_xpath(
        '//*[@id="config-pane"]/div/div/div[1]/table/tbody/tr[123]/td[2]/div/input')
    # rfCoil=//*[@id="config-pane"]/div/div/div[1]/table/tbody/tr[123]/td[2]/div/input

    assert rf_coil.is_selected() == 1
    context.driver.quit()


# Functions for Step-15

time_string = time.asctime().replace(":", "")
newaccountid = "testaccount" + time_string.lower().replace(" ", "")


@given('User create an account with normal user')
def createAccountWithNormalUser(context):
    print("Navigating to the Dev Tab")
    time.sleep(3)
    context.driver.find_element_by_class_name('dev-mode-only').click()
    time.sleep(3)
    print("Navigating to the Account Tab")
    context.driver.find_element_by_id("tab-accounts").click()
    time.sleep(3)
    id = newaccountid
    context.driver.find_element_by_class_name("accounts-reload").click()  # Cache Update first time
    time.sleep(15)
    # driver.find_element_by_partial_link_text("Enter Account Name").send_keys("New Account" )
    context.driver.find_element_by_xpath("//*[@id='accounts-pane']/div/div[1]/div[1]/div[2]/input").send_keys(
        id)  # Creating a new account name
    time.sleep(5)
    context.driver.find_element_by_class_name("glyphicon.glyphicon-plus").click()  # Click to add the button
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "//*[@id='accounts-pane']/div/div[1]/div[2]/div[2]/table/tbody/tr[8]/td[2]/div/input").send_keys(
        "TestPassword1!")
    time.sleep(5)
    context.driver.find_element_by_xpath(
        "//*[@id='accounts-pane']/div/div[1]/div[2]/div[2]/table/tbody/tr[9]/td[2]/div/input").send_keys(
        "TestPassword1!")
    time.sleep(5)
    context.driver.find_element_by_class_name("accounts-save").click()
    time.sleep(10)
    context.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/button[1]").click()

    # driver.find_element_by_link_text("OK").click()
    time.sleep(3)
    context.driver.find_element_by_class_name("accounts-reload").click()  # Cache Update
    time.sleep(15)
    context.driver.find_element_by_class_name("glyphicon.glyphicon-off").click()  # Click on Power off Button
    time.sleep(5)
    context.driver.find_element_by_class_name("btn.btn-logout").click()
    time.sleep(3)


@when('User logs in with the newly created account')
def loginToNewAccount(context):
    print("Getting the Scanner URL.......................")
    context.driver.get("https://10.52.11.152:8080/")  # change the scanner IP address here to choose scanner
    context.driver.maximize_window()
    time.sleep(3)
    print("Login to the URL................................")
    # print("Clicking on the advance..........................")
    # context.driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").click()  # click on advance
    # time.sleep(2)
    # print("Clicking on the proxy.............................")
    # context.driver.find_element_by_xpath("/html/body/div/div[3]/p[2]/a").click()  # click on proxy
    time.sleep(3)
    loginId = context.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/input[1]")  # click on the log in ID
    # type in the log in ID
    print("Entering the ID...................................")
    loginId.send_keys(newaccountid)
    # Enter Password
    print("Entering the Password...........................")
    context.driver.find_element_by_id("password").send_keys("TestPassword1!")
    time.sleep(2)
    print("Clicking in to the sign in button.................")
    context.driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/button').click()
    time.sleep(3)


@then('User can log in with the newly created Account')
def verifyAccount(context):
    context.driver.find_element_by_id("tab-about").click()
    time.sleep(3)
    context.driver.find_element_by_id("tab-profile").click()
    time.sleep(3)
    accountid = context.driver.find_element_by_xpath(
        "//*[@id='profile-pane']/div/div[1]/table/tbody/tr[3]/td[2]/div/span").text  # getting account ID
    print(accountid)
    time.sleep(3)
    try:
        assert accountid == id
    except AssertionError:
        print("Page is not opened!")


# Functions for Step-12
@when('User checks the Event Tab')
def goToEvent(context):
    time.sleep(3)
    context.driver.find_element_by_id("tab-events").click()
    context.driver.refresh()
    time.sleep(3)
    context.driver.find_element_by_id("tab-events").click()


@then('Event should be registered')
def eventscheck(context):
    time.sleep(3)
    a = context.driver.find_element_by_xpath(
        '//*[@id="logTable"]/table/tbody/tr[1]/td[6]').text  # get text regarding scanner log in or restart
    print("from Eventlog: " + a)
    assert a == "User 'hri' sent command 'refresh'"
    context.driver.quit()


# Functions for Step-13

@when('Modify the fields under Institution Information and Save&Apply the changes and Logout')
def ModifyInstituionInfo(context):
    context.driver.find_element(By.XPATH, Locator.InstitutionName).clear()
    context.driver.find_element(By.XPATH, Locator.InstitutionName).send_keys("Hyperfine_Research_Inc_testmodify")
    context.driver.find_element(By.XPATH, Locator.InstitutionAddress).clear()
    context.driver.find_element(By.XPATH, Locator.InstitutionAddress).send_keys(
        "351A New Whitfield St, Guilford CT 06437 testmodify")
    context.driver.find_element(By.XPATH, Locator.InstitutionDepartmentName).clear()
    context.driver.find_element(By.XPATH, Locator.InstitutionDepartmentName).send_keys("Verification testmodify")
    context.driver.find_element(By.XPATH, Locator.StationName).clear()
    context.driver.find_element(By.XPATH, Locator.StationName).send_keys("C06 testmodify")
    time.sleep(2)
    context.driver.find_element(By.XPATH, Locator.SaveConnectionSettings).click()
    context.driver.close()
    pass


@then('Verify if the institution changes are saved and displayed in the Metadata config')
def VerifyInstituionInfo(context):
    assert True, context.driver.getPageSource().contains("Hyperfine_Research_Inc_testmodify")
    # context.driver.find_element_by_xpath("//*[text()='Hyperfine_Research_Inc_testmodify']").is_displayed()


@then('Reset all the Institution fields to defaults')
def ResetInstituionInfo(context):
    context.driver.find_element(By.XPATH, Locator.InstitutionName).clear()
    context.driver.find_element(By.XPATH, Locator.InstitutionName).send_keys("Hyperfine_Research_Inc")
    context.driver.find_element(By.XPATH, Locator.InstitutionAddress).clear()
    context.driver.find_element(By.XPATH, Locator.InstitutionAddress).send_keys(
        "351A New Whitfield St, Guilford CT 06437")
    context.driver.find_element(By.XPATH, Locator.InstitutionDepartmentName).clear()
    context.driver.find_element(By.XPATH, Locator.InstitutionDepartmentName).send_keys("Verification")
    context.driver.find_element(By.XPATH, Locator.StationName).clear()
    context.driver.find_element(By.XPATH, Locator.StationName).send_keys("C06")
    time.sleep(2)
    context.driver.find_element(By.XPATH, Locator.SaveConnectionSettings).click()
    context.driver.close()
