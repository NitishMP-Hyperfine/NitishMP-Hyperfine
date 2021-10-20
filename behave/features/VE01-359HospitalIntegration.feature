Feature: Test functionality of pulling patient information-Hospital Integration

  Scenario: About VE01-359 Step 2 - Log in and start scanner
    Given Log in to Hyperfine URL on chrome
    When User Enter ID and PWD
    And Go to About tab and check the software version
    Then User must be logged out successfully

  Scenario: About VE01-359 Step 3 - Set Incorrect Connectivity metadata for MWL/PACS
    Given  User must be logged in successfully again
    When Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
    And Set the Pacs and MWL config fields with incorrect data
    And Go to Order List under Patients tab,Check MWL and PACS sever connection messages should be in RED color
    Then The Alarm indicator should display Connectivity to PACS/MWL, alarm is set


    Scenario: About VE01-359 Step 4 - Set Correct Connectivity metadata for MWL/PACS
      Given  User must be logged in successfully again
      When  Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
      And Set the Pacs and MWL config fields with correct data
      And Go to Order List under Patients tab,Check MWL and PACS sever connection messages should be in Green color
      Then Verify that no notifications should be present in the Alarms

   Scenario: About VE01-359 Step 5 - Patient info is updated under Worklist orders
     Given  User must be logged in successfully again
     When Go to Patient tab and open Order List page
     And  You click on Refresh order list and click on a Patient name
     Then  Confirm orders with patient info are updated and listed under Worklist orders

    Scenario: About VE01-359 Step 6 - Atleast three Patient data fields are filled
      Given  User must be logged in successfully again
      When Go to Patient tab and open Order List page
      And You click on Refresh order list and click on a Patient name
      Then Verify these fields are filled in- AccessionNumber,Modality,PatientBirthdate,PatientName

    Scenario: About VE01-359 Step 7 - Register a Patient
       Given  User must be logged in successfully again
       When Go to Patient tab and open Order List page
       And  You click on Refresh order list, click on a Patient name and Register the Patient
       Then Navigate to the Patient info tab and Verify if fields from the order list matches the Patient info tab

     Scenario: About VE01-359 Step 8 - Run a Localizer Sequence and complete exam
       Given  User must be logged in successfully again
       When   You Select and Register a patient
       And    Go to Exams tab and Select Sequences tab and Search Localizer sequence and click add and Start exam
       Then   Click the checkmark to complete the exam and upload the images

     Scenario: About VE01-359 Step 9- Clear Patient Data
       Given  User must be logged in successfully again
       When   You Select and Register a patient
       Then   Verify if the patient info is cleared from all the fields when Clear Patient Data is clicked

     Scenario: About VE01-359 Step 10- Set Connectivity metadata for a different MWL
       Given User must be logged in successfully again
       When Go to Configs tab on Dev page and select Metadata config from dropdown, Open and Expand all fields
       And  Set the MWL config fields with correct UK Dicom Server data and Check MWL and PACS sever connection messages
       Then The patients order list should be populated



