import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators import Locator



class DevPage(object):
    def OpenandExpandMetadataConfig(context):
        context.driver.find_element(By.CLASS_NAME, Locator.DevTab).click()
        context.driver.find_element(By.CLASS_NAME, Locator.DevModeSelectSendButton).click()
        time.sleep(2)
        context.driver.find_element(By.CLASS_NAME, Locator.DevModeSelectExpandAllButton).click()
        time.sleep(5)

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

    def VerifyFAT_TestResult(context):
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