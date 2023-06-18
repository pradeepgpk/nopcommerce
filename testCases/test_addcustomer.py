import time
import pytest
from pageObjects.Loginpage import Login
from pageObjects.AddcustomerPage import Addcustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
from selenium.webdriver.common.by import By

class Test_003_Addcustomer:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPasswordL()
    logger = LogGen.loggen()

    def test_addcustomer(self,setup):
        self.logger.info("********Test_003_AddCustomer************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login successful***********")

        self.logger.info("********** Starting Add customer Test **********************")

        self.addcust = Addcustomer(self.driver)

        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()

        self.addcust.ClickOnAddNew()

        self.logger.info("**********providing customer info************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.SetEmail(self.email)
        self.addcust.Setpassword("test123")
        self.addcust.SetFirstName("bala")
        self.addcust.SetLastName("pradeep")
        self.addcust.SetGender("Male")
        self.addcust.SetDob("8/24/2022")
        self.addcust.SetCompanyname("busyqa")

        self.addcust.SetCustomerRoles("Guests")
        time.sleep(2)
        self.addcust.SetManagerOfvender("Vendor 2")


        self.addcust.SetAdminContent(" this is for testing")
        self.addcust.ClickOnSave()

        self.logger.info("********* saving customer info*********")
        self.logger.info("******* Add customer validation started********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("********* Add customer test passed***********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("************* Add new customer test failed************")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Home Page Title Test***********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

