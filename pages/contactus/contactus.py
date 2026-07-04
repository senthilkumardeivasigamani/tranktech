class contactus:
    def __init__(self, page):
        self.page = page
        self.contact_us=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.mail=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.company=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.serviceDropDown=page.locator('(//select[@name="service"])[2]')
        self.phone=page.locator('(//input[@name="phone"])[2]')
        self.message=page.locator('(//textarea[@placeholder="Message"])[2]')

        #Slect DropDown locators
        self.countryDropDownselect=page.locator('//select[@id="countrySelector"]')

    def contactUsFill(self):
        self.contact_us.click()
        self.name.fill('Senthil')
        self.mail.fill('june.senthil@gmail.com')
        self.company.fill('Oracle')
        self.serviceDropDown.select_option("Web Development")
        self.phone.fill('9597777461')
        self.message.fill('My Automation Scripts...')
        self.page.wait_for_load_state("load")

    def countryDropDown(self):
        self.countryDropDownselect.select_option('India')
        self.page.wait_for_load_state(state="load")
        self.countryDropDownselect.select_option('USAA')
        self.page.wait_for_load_state("load")
        self.countryDropDownselect.select_option('UAEE')
        self.page.wait_for_load_state("load")
