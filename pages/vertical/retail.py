class retail:
    def __init__(self,page):
        self.page=page
        #Reatil and Ecommerce
        self.verticals=page.locator("(//a[text()='Verticals'])[1]")
        self.ret_ecomm=page.locator("//strong[text()='Retail and Ecommerce']")
        self.ecom_website=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.ecom_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

    def retailSubMenu(self):
        retailList=[self.ecom_website,self.ecom_app]
        for locator in retailList:
            self.verticals.hover()
            self.page.wait_for_timeout(500)
            self.ret_ecomm.hover()
            self.page.wait_for_timeout(500)
            locator.click()
            self.page.wait_for_load_state(state="load")
            self.page.go_back()
            self.page.wait_for_load_state(state="load")