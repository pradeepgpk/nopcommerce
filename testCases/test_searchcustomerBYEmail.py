import time

import pytest

from pageObjects.Loginpage import Login
from pageObjects.AddcustomerPage import Addcustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_SearchCustomerByEmail_004:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPasswordL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchcustomerByEmail(self,setup):
        self.logger.info("******** Search Customer BY Email 004************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful************")
        self.logger.info("******** Starting Search Customer By Email ************")

        self.addcust = Addcustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()
        time.sleep(3)

        self.logger.info("********* Searching customer By Email Id*******")
        searchcust = SearchCustomer(self.driver)
        searchcust.SetEmail("victoria_victoria@nopCommerce.com")
        searchcust.ClickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("********* tc_searchcustomerByEmail_004 Finished*******")
        self.driver.close()




