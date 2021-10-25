import time
from selenium.webdriver.common.by import By
from Locators import Locator



class PatientPage(object):
    def GotoOrderList(context):
        context.driver.find_element(By.ID, Locator.PatientTab).click()
        time.sleep(2)
        context.driver.find_element(By.ID, Locator.OderListTab).click()
        time.sleep(2)

    def SelectPatientOnly(context):
        context.driver.find_element(By.CLASS_NAME, Locator.RefreshOrderList).click()
        time.sleep(3)
        context.driver.find_element(By.XPATH, Locator.WorklistOrdersFirstPatient).click()
        time.sleep(3)

    def RegisterPatientOnly(context):
        context.driver.find_element(By.CLASS_NAME, Locator.RefreshOrderList).click()
        time.sleep(3)
        context.driver.find_element(By.XPATH, Locator.WorklistOrdersFirstPatient).click()
        time.sleep(3)
        context.driver.find_element(By.CLASS_NAME, Locator.RegisterPatient).click()
        time.sleep(3)

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

    def checkConnectedServerMsgs(context):
        context.driver.find_element(By.ID, Locator.PatientTab).click()
        context.driver.find_element(By.ID, Locator.OderListTab).click()
        context.driver.find_element(By.XPATH, Locator.ConnectedToMWLServerMessage).is_displayed()
        context.driver.find_element(By.XPATH, Locator.ConnectedToPACSServerMessage).is_displayed()
        time.sleep(5)

    def checkNotConnectedServerMsgs(context):
        context.driver.find_element(By.ID, Locator.PatientTab).click()
        context.driver.find_element(By.ID, Locator.OderListTab).click()
        context.driver.find_element(By.XPATH, Locator.NotConnectedToMWLServerMessage).is_displayed()
        context.driver.find_element(By.XPATH, Locator.NotConnectedToPACSServerMessage).is_displayed()
        time.sleep(3)