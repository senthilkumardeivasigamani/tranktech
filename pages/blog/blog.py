class blog:
    def __init__(self, page):
        self.page = page
        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.appDevelop=page.locator('//a[@href="/blog/category/app-development/"]')
        self.webDevelop=page.locator('//a[@href="/blog/category/web-development/"]')
        self.softwareDwelop=page.locator('//a[@href="/blog/category/software-development/"]')
        self.digitalMarket=page.locator('//a[@href="/blog/category/digital-marketing/"]')
        self.emailMarket=page.locator('//a[@href="/blog/category/email-marketing/"]')
        self.ai=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
        self.uiuxDesignb=page.locator('//a[@href="/blog/category/ui-ux-design/"]')
        self.appdev01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
        self.ai01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
        self.contmark01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
        self.crmDev01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
        self.digmark01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
        self.ecommdev01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
        self.emaimark01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
        self.grapdesig01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
        self.softItcmp01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
        self.softdev01=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
        self.uiux01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
        self.webDevelop01=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')

    def blogSubMenus(self):
        blogList=[self.appDevelop,self.webDevelop,self.softwareDwelop,self.digitalMarket,self.emailMarket,self.ai,self.uiuxDesignb,self.contmark01,self.crmDev01,self.digmark01,self.ecommdev01,self.emaimark01,self.grapdesig01,self.softItcmp01,self.softdev01,self.uiux01,self.webDevelop01]
        self.blog.click()
        self.page.wait_for_timeout(1000)
        for locator in blogList:
            locator.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()
            self.page.wait_for_load_state('load')
