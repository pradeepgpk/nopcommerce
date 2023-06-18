from selenium.webdriver.common.by import By
class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastname_id ="SearchLastName"
    btnSearch_Id ="search-customers"

    tbleSearchResult_xapth = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRow_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def SetEmail(self,email):
         self.driver.find_element(By.ID,self.txtEmail_id).clear()
         self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def SetFirstName(self,fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def SetLastName(self,lname):
        self.driver.find_element(By.ID, self.txtLastname_id).clear()
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lname)

    def ClickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_Id).click()

    def getNoofRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRow_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumn_xpath))

    def searchCustomerByEmail(self,email):
        flag = False
        for i in range(1,self.getNoofRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid = table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr['+str(i)+']/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr['+str(r)+']/td[3]").text
            if name ==Name:
                flag = True
                break
        return flag