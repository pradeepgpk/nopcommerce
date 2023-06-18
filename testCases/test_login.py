from pageObjects.Loginpage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
# from utilities import customLogger
class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPasswordL()
    logger = LogGen.loggen()

    # logger = customLogger.test_logDemo()
    def test_homePageTitle(self,setup):
        self.logger.info("***************** Test_001_Login ***********************")
        self.logger.info("***************** Verifying Home Page Title ***********************")
        self.driver =setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("***************** Home Page Title Test Is Passed ***********************")

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login_1.png")
            self.driver.close()
            self.logger.error("***************** Home Page Title Test Is Failed ***********************")
            assert False

    def test_login(self,setup):
        self.logger.info("***************** Verifying Login Test ***********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        loginpageobj = Login(self.driver)
        loginpageobj.setUserName(self.username)
        loginpageobj.setPassword(self.password)
        loginpageobj.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administratio":
            self.driver.close()
            assert True
            self.logger.info("***************** Login Title Test Passed ***********************")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login_2.png")
            self.driver.close()
            self.logger.error("***************** Login Title Test Failed ***********************")
            assert False

# pytest -v -s --html=Reports\report.html testCases/test_login.py
