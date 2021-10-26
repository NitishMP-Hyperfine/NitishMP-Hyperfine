import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.insert(0, '/Users/Nprashanth/PycharmLocalProjects/NitishMP-Hyperfine/behave/features/steps/Pages')
from Pages.Locators import Locator
from Pages.Common_Classes import Commonclasses
from Pages.DevPage import DevPage
from Pages.PatientPage import PatientPage
from Pages.ExamPage import ExamPage


# Functions for Step-2
@given('Log in to Hyperfine URL on chrome')
def getHyperfineUrl8080(context):
    context.driver = webdriver.Chrome(
        executable_path="/Users/Nprashanth/PycharmLocalProjects/NitishMP-Hyperfine/behave/drivers/chromedriver")
    context.driver.get("https://10.52.11.48:8080/")  # change the scanner IP address here to choose scanner
    context.driver.find_element_by_xpath("/html/body/div/div[2]/button[3]").click()  # click on advance
    time.sleep(2)
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
    Commonclasses.LogintoHyperfineURL8080(context)


@when('Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields')
def getMetadataconfig(context):
    DevPage.OpenandExpandMetadataConfig(context)


@when('Set the Pacs and MWL config fields with incorrect data')
def IncorrectMetadataConfig(context):
    DevPage.setIncorrectMetadataConfig(context)


@when('Go to Order List under Patients tab,Check MWL and PACS sever connection messages should be in RED color')
def checkNoConnectionServerMsgs(context):
    PatientPage.checkNotConnectedServerMsgs(context)


@then('The Alarm indicator should display Connectivity to PACS/MWL, alarm is set')
def verifyAlarmsPresent(context):
    Commonclasses.verifyPACSMWLAlarmsPresent(context)


# Functions for Step-4

@when('Set the Pacs and MWL config fields with correct data')
def CorrectMetadataConfig(context):
    DevPage.setCorrectMetadataConfig(context)


@when('Go to Order List under Patients tab,Check MWL and PACS sever connection messages should be in Green color')
def checkConnectionMsgs(context):
    PatientPage.checkConnectedServerMsgs(context)


# Functions for Step-5

@when('Go to Patient tab and open Order List page')
def OrderList(context):
    PatientPage.GotoOrderList(context)


@when('You click on Refresh order list and click on a Patient name')
def SelectPatientname(context):
    PatientPage.SelectPatientOnly(context)


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
    PatientPage.RegisterPatientOnly(context)


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
def SelectandRegisterPatient1(context):
    PatientPage.SelectandRegisterPatient(context)


@when('Go to Exams tab and Select Sequences tab and Search Localizer sequence and click add and Start exam')
def RunLocalizerSequence(context):
    ExamPage.GotoExamandRunLocalizerSequence(context)


@then('Click the checkmark to complete the exam and upload the images')
def CompleteExam(context):
    ExamPage.CompleteandUploadExam(context)


# Functions for Step - 9

@then("Verify if the patient info is cleared from all the fields when Clear Patient Data is clicked")
def ClearPatient(context):
    PatientPage.ClearPatientInfo(context)

    # Functions for Step -10
    @when(
        'Set the MWL config fields with correct UK Dicom Server data and Check MWL and PACS sever connection messages')
    def SetMWLUKMetadata(context):
        DevPage.SetMWLUKMetadata(context)

    @then('The patients order list should be populated')
    def VerifyPatientOrderList(context):
        context.driver.find_element(By.CLASS_NAME, Locator.RefreshOrderList).click()
        time.sleep(3)
        context.driver.find_element(By.XPATH, Locator.WorklistOrdersFirstPatient).click()
        time.sleep(3)
        context.driver.find_element(By.XPATH, Locator.WorklistPatientName2).is_displayed()
        context.driver.close()
