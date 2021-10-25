Feature: Scenario Template: his test verifies basic software functionality is unchanged between various software releases.
  @Step2
  Scenario: About VE01-284 Step 2 - Startup and Update
    Given Log in to Hyperfine Service Console on chrome
    When  Go to Updates under Service tab and Select and download the latest version to update and install
    Given User must be logged in successfully again
    When  Go to About tab and check the software version
    Then  User must be logged out successfully
  @Step4
  Scenario: About VE01-284 Step 4 - Verify no notification or alarms are present on login
    Given Log in to Hyperfine URL on chrome
    When  User Enter ID and PWD
    Then  Verify that no notifications should be present in the Alarms
  @Step5
  Scenario: About VE01-284 Step 5 - Verify About Feature
    Given  User must be logged in successfully again
    When   User checks the about tab
    Then   User able to take the screenshot of About
  @Step6
  Scenario: About VE01-284 Step 6 - Check for SPEC values
    Given  User must be logged in successfully again
    When User checks the about tab - Spec Values
    Then User able to take the screenshot of specs values

  @Step7
  Scenario:About VE01-284 Step 7 - Confirm Versions from About tab and Metadata revisions matches installed
    Given  User must be logged in successfully again
    When   Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
    Then   User gets a screenshot for the build information containing in metadata

  @Step8
  Scenario: About VE01-284 Step 8 - Confirm Same Versions are available in both Dev and Non-Dev mode on UI
    Given  User must be logged in successfully again
    Then   Verify the Software version and the Firmware/DLL matches in the Dev and Non-Dev mode of UI

  @Step9
  Scenario: About VE01-284 Step 9 - Verify if rf_coil value is set and coil_autoselect is checked
    Given  User must be logged in successfully again
    When  Verify if rf_coil value is set and coil_autoselect is checked in the Metadata
    Then  rf_coil is autoselected

  @Step12
   Scenario: About VE01-284 Step 12 - Verify if Events tab is logging all actions and usernames
    Given  User must be logged in successfully again
    When   User checks the Event Tab
    Then   Event should be registered

  @Step13
  Scenario: About VE01-359 Step 13 - Verify changes to Institution Info under Console in Metadata is saved
    Given  User must be logged in successfully again
    When   Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
    And    Modify the fields under Institution Information and Save&Apply the changes and Logout
    Given  User must be logged in successfully again
    When   Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
    Then   Verify if the institution changes are saved and displayed in the Metadata config
    Then   Reset all the Institution fields to defaults

  @Step14
  Scenario: About VE01-359 Step 14 - Verify Email and Data Upload settings are enabled and cloud credentials are set
    Given  User must be logged in successfully again
    When   Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
    Then   Configure ProxyServerURL,DeviceAccess,UploadToCloudPACSandLocalPACS,UncheckDeIdentifyUploadsToPACS,SuppressAllPHI,UploadDeviceTelemetryAndRawData,EnableElasticFileBeatAndEmailNotifications

  @Step15
  Scenario:About VE01-359 Step 15 - Create a New User from Accounts
    Given User must be logged in successfully again
    And   User create an account with normal user
    When  User logs in with the newly created account
    Then  User can log in with the newly created Account

  @Step16
  Scenario: About VE01-359 Step 16 - Accounts Management Cloud
    Given  User must be logged in to Account Management Cloud
    When   Add the new user to an organization
    And    User must be logged in successfully again
    And    Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
    Then   Verify if the valid metadata is filled in and Organization and new accounts are loaded from the cloud on Accounts tab

   @Step17
   Scenario: About VE01-359 Step 17 - Verify Telemetry
   Given  User must be logged in successfully again
   When   Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
   And    Configure and Enable ElasticFileBeat and Elastic API key is set
   Then   Go to Events tab and verify metadata event has been registered
   Then   Verify Events are present for FM solution on Kibana

  @Step18
  Scenario: About VE01-359 Step 18,19,20 - Hospital Integration
    Given  User must be logged in successfully again
    When   Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
    And    Set the Pacs and MWL config fields with correct data
    And    Go to Order List under Patients tab,Check MWL and PACS sever connection messages should be in Green color
    Then   Verify that no notifications should be present in the Alarms

  @Step22
  Scenario: About VE01-359 Step 22 - Uploader and Email Notification
    Given  User must be logged in successfully again
    When   You Select and Register a patient
    And    Go to Exams tab and Select Sequences tab and Search Localizer sequence and click add and Start exam
    Then   Click the checkmark to complete the exam and upload the images
    Then   Verify if the email notifications were configured and received

  @Step23
  Scenario: About VE01-359 Step 23 - Verify Study is uploaded to Local PACS and cloud
    Given  User must be logged in to LOCAL PACS and verify if the study is uploaded to the cloud

  @Step26
  Scenario: About VE01-359 Step 26 - Load FAT Phantom and execute Final Assembly Test
    Given  User must be logged in successfully again
    Then   Go to Self Test under DEV tab and execute the Final Assembly Test with the FAT phantom successfully
