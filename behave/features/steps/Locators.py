from selenium.webdriver.common.by import By


class Locator:
    # Sign-In Page Locators
    username = "//input[@id='user']"
    password = "//input[@id='password']"
    SignInButton = "//button[@class='signin btn btn-lg btn-primary btn-block']"

    USRNME = (By.ID, "user")
    PWD = (By.ID, "password")
    SignIN = (By.CLASS_NAME, "signin btn btn-lg btn-primary btn-block")

    # Home Page Locators
    HyperfineLogo = "//*[@id='tab-logo']"
    DevTab = "dev-mode-only"  # ClassName
    ExpertTab = "expert-mode-only"  # ClassName
    PatientTab = "tab-subject"  # ByID
    ExamTab = "tab-exam"  # ByID
    ScanTab = "tab-scan"  # ByID
    ThreeDTab = "tab-volume"  # ByID
    StatusTab = "tab-status"  # ByID
    LinksTab = "tab-links"  # ByID
    EventsTab = "tab-events"  # ByID
    AboutTab = "tab-about"  # ByID
    AlarmsButton = "//*[@id='alarms']"
    AlarmMenu = "//ul//li[contains(text(),'There are no current alarms')]"
    NoPACSServerConnectionMessageAlarm = "//span[contains(text(),'No PACS Server Connection')]"
    NoMWLServerConnectionMessageAlarm = "//span[contains(text(),'No MWL Server Connection')]"
    UserProfileButton = "/html/body/nav/ul/li[13]/button"
    PowerButton = "/html/body/nav/ul/li[14]/button"

    # Dev Page Locators

    # Config Page Locators
    ConfigTab = "//*[@id='tab-config']"
    DevModeListSelect = "list-category dev-mode-only"  # ClassName
    DevModeSelectSendButton = "button-send"  # ClassName
    DevModeSelectExpandAllButton = "button-expand"  # ClassNAme
    MWLAETitle = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[43]/td[2]/div/input"
    MWLAEAddress = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[44]/td[2]/div/input"
    MWLAEPort = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[45]/td[2]/div/input"
    PacsAETitle = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[36]/td[2]/div/input"
    PacsAEAddress = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[37]/td[2]/div/input"
    PacsAEPort = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[38]/td[2]/div/input"
    SaveConnectionSettings = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[77]/td[1]/div/button"
    Version = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[4]/td[2]/div/span"
    Datestamp = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[5]/td[2]/div/span"
    FirmwareDLLversionMetadata = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[11]/td[2]/div/span"
    InstitutionName = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[72]/td[2]/div/input"
    InstitutionAddress = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[73]/td[2]/div/input"
    InstitutionDepartmentName = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[74]/td[2]/div/input"
    StationName = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[75]/td[2]/div/input"
    ProxyServerURL = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[17]/td[2]/div/input"
    DeviceUsername = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[24]/td[2]/div/input"
    DevicePassword = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[25]/td[2]/div/input"
    DeviceOrg = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[26]/td[2]/div/input"
    UplaodToCloudPACS = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[31]/td[2]/div/input"
    PushToLocalPACSCheckbox = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[34]/td[2]/div/input"
    DeIdentifyUploadsLocalPACS = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[35]/td[2]/div/input"
    DeIdentifyUploadsCloudPACS = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[32]/td[2]/div/input"
    SuppressAllPHI = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[49]/td[2]/div/input"
    UploadDeviceTelemetry = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[55]/td[2]/div/input"
    UploadDeviceRawdata = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[57]/td[2]/div/input"
    UploadDeviceRawdataDirectly = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[58]/td[2]/div/input"
    EnableElasticFilebeat = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[60]/td[2]/div/input"
    ElasticAPIKey = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[61]/td[2]/div/input"
    EnableEmailNotifications = "//*[@id='config-pane']/div/div/div[1]/table/tbody/tr[70]/td[2]/div/input"

    # Accounts Page Locators
    AccountsTab = "//*[@id='tab-accounts']"

    # Signal Page Locators
    SignalTab = "//*[@id='tab-graph']"

    # Noise Page Locators
    NoiseTab = "//*[@id='tab-powgraph']"

    # Temps Page Locators
    TempsTab = "//*[@id='tab-temp']"

    # Dev_Sequence Page Locators
    DevSequenceTab = "//*[@id='tab-sequence']"

    # Self Test Page Locators
    SelfTestTab = "//*[@id='tab-diagnostics']"
    SelfTestExpandAll = "//*[@id='diag_editor']/button[2]"
    SelectTestGroup = "//*[@id='diag_editor']/table/tbody/tr[2]/td[2]/div/select"
    RunSelfTest = "//button[contains(text(),'Run Tests')]"
    ClearALLSelfTest = 'button-diagnostics-clear'  # BY Class Name
    ResetViewSelfTest = "button-reset"  # BY Class Name
    # FAT Test Locators
    UpdateCoilFileTest = "//*[@id='diag_editor']/table/tbody/tr[15]/td[2]/div/span"
    NoiseTest = "//*[@id='diag_editor']/table/tbody/tr[22]/td[2]/div/span"
    CenterFrequencyTest = "//*[@id='diag_editor']/table/tbody/tr[69]/td[2]/div/span"
    AutoShimTest = "//*[@id='diag_editor']/table/tbody/tr[86]/td[2]/div/span"
    RFPowerCalTest = "//*[@id='diag_editor']/table/tbody/tr[101]/td[2]/div/span"
    ImagingTest0 = "//*[@id='diag_editor']/table/tbody/tr[120]/td[2]/div/span"
    ImagingTest1 = "//*[@id='diag_editor']/table/tbody/tr[179]/td[2]/div/span"
    ImagingTest2 = "//*[@id='diag_editor']/table/tbody/tr[261]/td[2]/div/span"
    ImagingTest3 = "//*[@id='diag_editor']/table/tbody/tr[324]/td[2]/div/span"

    # Expert Page Locators

    # Patient Page Locators
    OderListTab = "tab-worklist"  # ByID
    NotConnectedToMWLServerMessage = "//*[@id='worklist-pane']/div/div[1]/div[5]/span[2]"
    NotConnectedToPACSServerMessage = "//*[@id='worklist-pane']/div/div[1]/div[5]/span[7]"
    ConnectedToMWLServerMessage = "//*[@id='worklist-pane']/div/div[1]/div[5]/span[1]"
    ConnectedToPACSServerMessage = "//*[@id='worklist-pane']/div/div[1]/div[5]/span[6]"
    Notifications = "//*[@id='tab-email']"
    RefreshOrderList = "button-refresh-order-list"  # By ClassName
    WorklistOrdersFirstPatient = "//ul[@class = 'worklist-orders patientlist list-box unselectable']//li[1]"
    RegisterPatient = "button-register-patient"  # By ClassName
    PatientInfoTab = "tab-patient"  # By ClassName
    WorklistPatientName = "//table[@class='json-table']//tr[7]//span[contains(text(),'Allen Iverson')]"
    WorkListAccessionNum = "//table[@class='json-table']//tr[1]//span[contains(text(),'12345671')]"
    WorkListModality = "//table[@class='json-table']//tr[4]//span[contains(text(),'MR')]"
    WorkListDOB = "//table[@class='json-table']//tr[5]//span[contains(text(),'Jan 1, 2000')]"
    PatientInfoAccessionNum = "//*[@id='patient-pane']/div/table/tbody/tr[9]/td[2]/div/input"
    PatientInfoMRNNum = "//*[@id='patient-pane']/div/table/tbody/tr[3]/td[2]/div/input"
    PatientInfoFullName = "//*[@id='patient-pane']/div/table/tbody/tr[4]/td[2]/div/input"
    PatientInfoDOB = "//*[@id='patient-pane']/div/table/tbody/tr[5]/td[2]/div/input"
    PatientInfoSex = "//*[@id='patient-pane']/div/table/tbody/tr[6]/td[2]/div/select/option[2]"
    PatientInfoPerformingPhysician = "//*[@id='patient-pane']/div/table/tbody/tr[10]/td[2]/div/input"
    ClearPatientData = "//button[contains(text(),'Clear Patient Data')]"

    # EXAM Page Locators
    ExamSequencesTab = "tab-sequences"  # By ID
    ExamProtocolsTab = "tab-protocols"  # By ID
    ExamSequenceSearch = "//*[@id='search-input']"
    LocalizerSequence = "//*[@id='sequences-list']/a[106]"
    StartExam = "/html/body/nav/div[1]/div[1]/div/button[1]"
    CompleteExam = "/html/body/nav/div[1]/div[1]/div/button[6]"
    UploadNotificationBadge = "/html/body/nav/div[1]/div[1]/div/div[2]/div"
    ClearAll = "//button[contains(text(),'Clear All')]"
    # SCAN  Page Locators

    # 3D Page Locators

    # Status Page Locators

    # Links Page Locators

    # Events Page Locators
    MetadataEvent = '//*[@id="logTable"]/table/tbody/tr[1]/td[6]'
    # About Page Locators
    SoftwareBuild = "//*[@id='device-pane']/div/table/tbody/tr[4]/td[2]/div/span"
    FirmwareDLLVersion = "//*[@id='device-pane']/div/table/tbody/tr[10]/td[2]/div/span"

    # ServiceConsolePage
    # Service Page Locators
    UpdatesTab = "tab-updates"  # BY ID
    InstallationTab = "tab-installation"  # BY ID
    StatusTab = "tab-ctrl"  # BY ID
    LatestSWUpdate = "//*[@id='updates-pane']/div/div[3]/a[last()]"
    DownlaodUpdateButton = "(//a[contains(text(),'Download')])[last()]"
    InstallPackg = "//button[contains(text(),'Install Package')]"

    # ElasticSearch Staging Page Locators
    LogintoElasticSearch = "//p[contains(text(), 'Log in with Elasticsearch')]"
    ElasticSearchUsrnme = "//input[contains(@name, 'username')]"
    ElasticSearchPwd = "//input[contains(@name, 'password')]"
    ElasticSearchLoginButton = "//button[@class = 'euiButton euiButton--primary euiButton--fill']"
    Kibana = "//*[contains(text(),'Kibana')]"
    DiscoverKibana = "//*[contains(text(),'Discover')]"
    KibanaSearch = "//textarea[@placeholder = 'Search']"
    HostnameinTable = "//table/tbody//tr[1]//td[3]//*[contains(text(),'HG19480006')]"
    RefreshButton = "//button[@data-test-subj = 'querySubmitButton']"

    # GMAIL Login Locators
    Gmailusername = "identifierId" # By ID
    GmailNext = "//button[@class = 'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']"
    GmailPassword = "//input[@name = 'password']"
    GmailSigninButton = "//*[@id='signIn']"
    FirstGmail = "//span[@email='lucy@hyperfine.io']"
