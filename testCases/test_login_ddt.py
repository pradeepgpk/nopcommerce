import time
from pageObjects.Loginpage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseurl = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_loin_ddt(self,setup):
        self.logger.info("***************** Test_002_DDT_Login ***********************")
        self.logger.info("***************** Verifying Login DDT Test ***********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        loginpageobj = Login(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in a Excel :",self.rows)
        lst_status=[]  #empty list variable
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password= XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            loginpageobj.setUserName(self.user)
            loginpageobj.setPassword(self.password)
            loginpageobj.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Passed*******")
                    loginpageobj.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Failed*******")
                    loginpageobj.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****failed*******")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*****passed*******")
                    lst_status.append("Pass")
        if "fail" not in lst_status:
            self.logger.info("login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("*********** End of Login DDT Test ******************")
        self.logger.info("************** Completed Test_002_DDT_Login *********************")





