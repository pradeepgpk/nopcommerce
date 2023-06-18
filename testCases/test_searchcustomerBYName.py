import time

import pytest

from pageObjects.Loginpage import Login
from pageObjects.AddcustomerPage import Addcustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPasswordL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchcustomerByName(self,setup):
        self.logger.info("******** Search Customer BY Name 005************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful************")
        self.logger.info("******** Starting Search Customer By Name ************")

        self.addcust = Addcustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        time.sleep(2)
        self.addcust.ClickOnCustomersMenuItem()
        time.sleep(3)

        self.logger.info("********* Searching customer By Name*******")
        searchcust = SearchCustomer(self.driver)
        searchcust.SetFirstName("Victoria")
        searchcust.SetLastName("Terces")
        searchcust.ClickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("********* tc_searchcustomerByName_005 Finished*******")
        self.driver.close()

