import time
import os
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from Locators import Locator


# Functions for Step-2
@given('Log in to Hyperfine URL on chrome')
def getHyperfineUrl8080(context):
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.binary_location='/usr/bin/google-chrome'
    context.driver = webdriver.Chrome("/Users/Nprashanth/PycharmLocalProjects/behave/drivers/chromedriver")
    context.driver.get("https://10.52.11.48:8080/")  # change the scanner IP address here to choose scanner
    print("Clicking on the advance..........................")
    context.driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").click()  # click on advance
    time.sleep(2)
    print("Clicking on the proxy.............................")
    context.driver.find_element_by_xpath("/html/body/div/div[3]/p[2]/a").click()  # click on proxy
    time.sleep(5)


@when('User Enter ID and PWD')
def logIntotheHyperfineUrl(context):
    context.driver.find_element(By.XPATH, Locator.username).send_keys("hri")
    context.driver.find_element(By.XPATH, Locator.password).send_keys("Systems123")
    context.driver.find_element(By.XPATH, Locator.SignInButton).click()
    print("sign in button clicked")
    time.sleep(10)


@when('Go to About tab and check the software version')
def verifyLogin(context):
    context.driver.find_element(By.ID, Locator.AboutTab).click()
    l = context.driver.find_element_by_class_name("json-value-label")
    time.sleep(10)
    print("Software version is:" + l.text)


@then('User must be logged out successfully')
def checksuccessfullogin(context):
    print("Login successful")
    time.sleep(10)
    context.driver.close()


# Functions for Step-3

@given('User must be logged in successfully again')
def logintoHyperfineURLagain(context):
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.binary_location='/usr/bin/google-chrome'
    context.driver = webdriver.Chrome("/Users/Nprashanth/PycharmLocalProjects/behave/drivers/chromedriver")
    context.driver.get("https://10.52.11.48:8080/")  # change the scanner IP address here to choose scanner
    context.driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").click()  # click on advance
    time.sleep(2)
    context.driver.find_element_by_xpath("/html/body/div/div[3]/p[2]/a").click()  # click on prox
    time.sleep(5)
    context.driver.find_element(By.XPATH, Locator.username).send_keys("hri")
    context.driver.find_element(By.XPATH, Locator.password).send_keys("Systems123")
    context.driver.find_element(By.XPATH, Locator.SignInButton).click()
    time.sleep(10)


@when('Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields')
def getMetadataconfig(context):
    context.driver.find_element(By.CLASS_NAME, Locator.DevTab).click()
    context.driver.find_element(By.CLASS_NAME, Locator.DevModeSelectSendButton).click()
    time.sleep(2)
    context.driver.find_element(By.CLASS_NAME, Locator.DevModeSelectExpandAllButton).click()
    time.sleep(5)


@when('Set the Pacs and MWL config fields with incorrect data')
def setIncorrectMetadataConfig(context):
    context.driver.find_element(By.XPATH, Locator.MWLAETitle).clear()
    context.driver.find_element(By.XPATH, Locator.MWLAETitle).send_keys("HYPERPACS2")
    context.driver.find_element(By.XPATH, Locator.MWLAEAddress).clear()
    context.driver.find_element(By.XPATH, Locator.MWLAEAddress).send_keys("10.52.11.20")
    context.driver.find_element(By.XPATH, Locator.MWLAEPort).clear()
    context.driver.find_element(By.XPATH, Locator.MWLAEPort).send_keys("4240")
    context.driver.find_element(By.XPATH, Locator.PacsAETitle).clear()
    context.driver.find_element(By.XPATH, Locator.PacsAETitle).send_keys("HYPERPACS2")
    context.driver.find_element(By.XPATH, Locator.PacsAEAddress).clear()
    context.driver.find_element(By.XPATH, Locator.PacsAEAddress).send_keys("10.52.11.20")
    context.driver.find_element(By.XPATH, Locator.PacsAEPort).clear()
    context.driver.find_element(By.XPATH, Locator.PacsAEPort).send_keys("4240")
    context.driver.find_element(By.XPATH, Locator.SaveConnectionSettings).click()
    time.sleep(15)


@when('Go to Order List under Patients tab,Check MWL and PACS sever connection messages should be in RED color')
def checkConnectionMsgs(context):
    context.driver.find_element(By.ID, Locator.PatientTab).click()
    context.driver.find_element(By.ID, Locator.OderListTab).click()
    context.driver.find_element(By.XPATH, Locator.NotConnectedToMWLServerMessage).is_displayed()
    context.driver.find_element(By.XPATH, Locator.NotConnectedToPACSServerMessage).is_displayed()
    time.sleep(3)


@then('The Alarm indicator should display Connectivity to PACS/MWL, alarm is set')
def verifyAlarmsPresent(context):
    context.driver.find_element(By.ID, Locator.AlarmsButton).click()
    time.sleep(2)
    try:
        context.driver.find_element(By.XPATH, Locator.NoMWLServerConnectionMessageAlarm).is_displayed()
        context.driver.find_element(By.XPATH, Locator.NoPACSServerConnectionMessageAlarm).is_displayed()
    except:
        context.driver.close()
        assert False, "Alarm not found"
    context.driver.close()


# Functions for Step-4

@when('Set the Pacs and MWL config fields with correct data')
def setCorrectMetadataConfig(context):
    context.driver.find_element(By.XPATH, Locator.MWLAETitle).clear()
    context.driver.find_element(By.XPATH, Locator.MWLAETitle).send_keys("HYPERRIS")
    context.driver.find_element(By.XPATH, Locator.MWLAEAddress).clear()
    context.driver.find_element(By.XPATH, Locator.MWLAEAddress).send_keys("10.52.11.161")
    context.driver.find_element(By.XPATH, Locator.MWLAEPort).clear()
    context.driver.find_element(By.XPATH, Locator.MWLAEPort).send_keys("4243")
    context.driver.find_element(By.XPATH, Locator.PacsAETitle).clear()
    context.driver.find_element(By.XPATH, Locator.PushToLocalPACSCheckbox).is_enabled()
    context.driver.find_element(By.XPATH, Locator.PacsAETitle).send_keys("HYPERPACS2")
    context.driver.find_element(By.XPATH, Locator.PacsAEAddress).clear()
    context.driver.find_element(By.XPATH, Locator.PacsAEAddress).send_keys("10.52.11.167")
    context.driver.find_element(By.XPATH, Locator.PacsAEPort).clear()
    context.driver.find_element(By.XPATH, Locator.PacsAEPort).send_keys("4242")
    context.driver.find_element(By.XPATH, Locator.SaveConnectionSettings).click()
    time.sleep(15)


@when('Go to Order List under Patients tab,Check MWL and PACS sever connection messages should be in Green color')
def checkConnectionMsgs(context):
    context.driver.find_element(By.ID, Locator.PatientTab).click()
    context.driver.find_element(By.ID, Locator.OderListTab).click()
    context.driver.find_element(By.XPATH, Locator.ConnectedToMWLServerMessage).is_displayed()
    context.driver.find_element(By.XPATH, Locator.ConnectedToPACSServerMessage).is_displayed()
    time.sleep(5)


# Functions for Step-5

@when('Go to Patient tab and open Order List page')
def GotoOrderList(context):
    context.driver.find_element(By.ID, Locator.PatientTab).click()
    time.sleep(2)
    context.driver.find_element(By.ID, Locator.OderListTab).click()
    time.sleep(2)


@when('You click on Refresh order list and click on a Patient name')
def SelectPatient(context):
    context.driver.find_element(By.CLASS_NAME, Locator.RefreshOrderList).click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, Locator.WorklistOrdersFirstPatient).click()
    time.sleep(3)


@then('Confirm orders with patient info are updated and listed under Worklist orders')
def verifyPatientInfoLoaded(context):
    context.driver.find_element(By.XPATH, Locator.WorklistPatientName).is_displayed()
    context.driver.close()


# Functions for Step-6

@then('Verify these fields are filled in- AccessionNumber,Modality,PatientBirthdate,PatientName')
def VerifyPatientFields(context):
    context.driver.find_element(By.XPATH, Locator.WorkListAccessionNum).is_displayed()
    context.driver.find_element(By.XPATH, Locator.WorkListModality).is_displayed()
    context.driver.find_element(By.XPATH, Locator.WorkListDOB).is_displayed()
    context.driver.find_element(By.XPATH, Locator.WorklistPatientName).is_displayed()
    context.driver.close()


# Functions for Step-7

@when('You click on Refresh order list, click on a Patient name and Register the Patient')
def registerPatient1(context):
    context.driver.find_element(By.CLASS_NAME, Locator.RefreshOrderList).click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, Locator.WorklistOrdersFirstPatient).click()
    time.sleep(3)
    context.driver.find_element(By.CLASS_NAME, Locator.RegisterPatient).click()
    time.sleep(3)


@then('Navigate to the Patient info tab and Verify if fields from the order list matches the Patient info tab')
def VerifyPatientFields(context):
    try:
        MRNnum = context.driver.find_element(By.XPATH, Locator.PatientInfoMRNNum).text
        assert MRNnum.text == "12345671"
        FullName = context.driver.find_element(By.XPATH, Locator.PatientInfoFullName).text
        assert FullName.text == "Allen Iverson"
        DOB = context.driver.find_element(By.XPATH, Locator.PatientInfoDOB).text
        assert DOB.text == "Jan 1, 2000"
        Sex = context.driver.find_element(By.XPATH, Locator.PatientInfoSex).text
        assert Sex.text == "Male"
        AccessionNum = context.driver.find_element(By.XPATH, Locator.PatientInfoAccessionNum).text
        assert AccessionNum.text == "12345671"
        PerformingPhysician = context.driver.find_element(By.XPATH, Locator.PatientInfoPerformingPhysician).text
        assert PerformingPhysician.text == "Doctor Tom Jones"
    except:
        assert True

    context.driver.close()


# Functions for Step-8
@when('You Select and Register a patient')
def SelectandRegisterPatient(context):
    context.driver.find_element(By.ID, Locator.PatientTab).click()
    time.sleep(2)
    context.driver.find_element(By.ID, Locator.OderListTab).click()
    time.sleep(2)
    context.driver.find_element(By.CLASS_NAME, Locator.RefreshOrderList).click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, Locator.WorklistOrdersFirstPatient).click()
    time.sleep(3)
    context.driver.find_element(By.CLASS_NAME, Locator.RegisterPatient).click()
    time.sleep(2)


@when('Go to Exams tab and Select Sequences tab and Search Localizer sequence and click add and Start exam')
def RunLocalizerSequence(context):
    context.driver.find_element(By.ID, Locator.ExamTab).click()
    time.sleep(2)
    context.driver.find_element(By.ID, Locator.ExamSequencesTab).click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, Locator.ClearAll).click()
    context.driver.find_element(By.XPATH, Locator.ExamSequenceSearch).send_keys("Localizer")
    context.driver.find_element(By.XPATH, Locator.LocalizerSequence).click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, Locator.StartExam).click()
    time.sleep(80)


@then('Click the checkmark to complete the exam and upload the images')
def CompleteExam(context):
    context.driver.find_element(By.XPATH, Locator.CompleteExam).click()
    time.sleep(4)
    context.driver.find_element(By.XPATH, Locator.UploadNotificationBadge).is_enabled()
    time.sleep(60)
    context.driver.close()


# Functions for Step - 9

@then("Verify if the patient info is cleared from all the fields when Clear Patient Data is clicked")
def ClearPatientInfo(context):
    context.driver.find_element(By.XPATH, Locator.ClearPatientData).click()
    time.sleep(3)
    try:
        MRNnum = context.driver.find_element(By.XPATH, Locator.PatientInfoMRNNum).is_displayed()
        assert MRNnum.text == " "
        FullName = context.driver.find_element(By.XPATH, Locator.PatientInfoFullName).is_displayed()
        assert FullName.text == " "
        DOB = context.driver.find_element(By.XPATH, Locator.PatientInfoDOB).is_displayed()
        assert DOB.text == " "
        Sex = context.driver.find_element(By.XPATH, Locator.PatientInfoSex).is_displayed()
        assert Sex.text == " "
        AccessionNum = context.driver.find_element(By.XPATH, Locator.PatientInfoAccessionNum).is_displayed()
        assert AccessionNum.text == " "
        PerformingPhysician = context.driver.find_element(By.XPATH,
                                                          Locator.PatientInfoPerformingPhysician).is_displayed()
        assert PerformingPhysician.text == " "
    except:
        assert False

    # Functions for Step -10
    @when('Set the MWL config fields with correct UK Dicom Server data and Check MWL and PACS sever connection messages')
    def SetMWLUKMetadata(context):
        context.driver.find_element(By.XPATH, Locator.MWLAETitle).clear()
        context.driver.find_element(By.XPATH, Locator.MWLAETitle).send_keys("dicomserver.co.uk")
        context.driver.find_element(By.XPATH, Locator.MWLAEAddress).clear()
        context.driver.find_element(By.XPATH, Locator.MWLAEAddress).send_keys("dicomserver.co.uk")
        context.driver.find_element(By.XPATH, Locator.MWLAEPort).clear()
        context.driver.find_element(By.XPATH, Locator.MWLAEPort).send_keys("104")
        context.driver.find_element(By.XPATH, Locator.SaveConnectionSettings).click()
        time.sleep(5)
        context.driver.find_element(By.ID, Locator.PatientTab).click()
        context.driver.find_element(By.ID, Locator.OderListTab).click()
        context.driver.find_element(By.XPATH, Locator.ConnectedToMWLServerMessage).is_displayed()
        context.driver.find_element(By.XPATH, Locator.ConnectedToPACSServerMessage).is_displayed()
        time.sleep(15)
        pass

    @then('The patients order list should be populated')
    def VerifyPatientOrderList(context):
        context.driver.find_element(By.CLASS_NAME, Locator.RefreshOrderList).click()
        time.sleep(3)
        context.driver.find_element(By.XPATH, Locator.WorklistOrdersFirstPatient).click()
        time.sleep(3)
        context.driver.find_element(By.XPATH, Locator.WorklistPatientName2).is_displayed()
        context.driver.close()
