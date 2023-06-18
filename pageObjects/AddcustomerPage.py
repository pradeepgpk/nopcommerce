import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
class Addcustomer:

    lnkcustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkcustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"

    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtemail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtCustomerRole_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    drpMgrOfVender_xpath ="//select[@id='VendorId']"

    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath ="//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def ClickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkcustomers_menu_xpath).click()

    def ClickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkcustomers_menuitem_xpath).click()


    def ClickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def SetEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtemail_xpath).send_keys(email)

    def Setpassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def SetFirstName(self,firstname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstname)

    def SetLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastname_xpath).send_keys(lastname)

    def SetGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID,self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def SetDob(self,dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def SetCompanyname(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def SetCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRole_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Administators':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role =='Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def SetManagerOfvender(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drpMgrOfVender_xpath))
        drp.select_by_visible_text(value)

    def SetAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()

