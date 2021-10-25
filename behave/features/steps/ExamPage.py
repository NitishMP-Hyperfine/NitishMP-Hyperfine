import time
from selenium.webdriver.common.by import By
from Locators import Locator



class ExamPage(object):
    def GotoExamandRunLocalizerSequence(context):
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

    def CompleteandUploadExam(context):
        context.driver.find_element(By.XPATH, Locator.CompleteExam).click()
        time.sleep(4)
        context.driver.find_element(By.XPATH, Locator.UploadNotificationBadge).is_enabled()
        time.sleep(60)
        context.driver.close()

