class aboutus:
    def __init__(self, page):
        self.page = page
        self.about=page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')
        self.cmsWebsite=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.customWebPortaDev=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.mobileAppDesign=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsiveWebDesig=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brandIdentityDesign=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
        self.iosAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.hybridMobileapp=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.crossPlatfromApp=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.progressiveWebApp=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
        self.logodesign=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.bannerdesign=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packgingDesign=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.cardDesign=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
        
        #new page Locators
        self.arrow1=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        self.arrow2=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        self.website=page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
        self.androidAppDev=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.appDeve=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')

        
    def aboutUsSUbPage(self):
        aboutUsList=[self.cmsWebsite,self.customWebPortaDev,self.mobileAppDesign,self.responsiveWebDesig,self.brandIdentityDesign,self.iosAppDev,self.hybridMobileapp,self.crossPlatfromApp,self.progressiveWebApp,self.logodesign,self.bannerdesign,self.packgingDesign,self.cardDesign]
        for locator in aboutUsList:
            self.about.click()
            self.page.wait_for_load_state("load")
            locator.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")
    
    def aboutUsArrow(self):
        #self.website opening
        self.about.click()
        self.page.wait_for_load_state("load")
        self.arrow1.click()
        self.page.wait_for_load_state("load")
        self.website.click()
        new_page_event = self.page.context.wait_for_event("page")
        new_tab = new_page_event
        new_tab.wait_for_load_state("load")
        new_tab.close()
        
        #self.androidAppDev opening
        self.arrow2.click()
        self.page.wait_for_load_state("load")
        self.androidAppDev.click()
        new_page_event = self.page.context.wait_for_event("page")
        new_tab = new_page_event
        new_tab.wait_for_load_state("load")
        new_tab.close()
        
        # #self.appDeve opening
        self.appDeve.click()
        new_page_event = self.page.context.wait_for_event("page")
        new_tab = new_page_event
        new_tab.wait_for_load_state("load")
        new_tab.close()


        '''this failing becaue i eas clickong only the first arrow and not the second arrow so the locators are not visible need to find a way to click the second arrow and then click the locators'''

        # self.about.click()
        # self.page.wait_for_load_state("load")
        # self.arrow1.click()
        # self.page.wait_for_load_state("load")        
        # self.arrowDropDoenList=[self.website,self.androidAppDev,self.appDeve]
        # for locator in self.arrowDropDoenList:
        #     with self.page.context.expect_page() as new_page_info:
        #         locator.click()
        #     new_tab = new_page_info.value
        #     new_tab.wait_for_load_state("load")
        #     new_tab.close()
        
