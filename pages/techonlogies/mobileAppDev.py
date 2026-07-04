class mobileAppDev:
    def __init__(self,page):
        self.page=page
        self.technologies=page.locator("(//a[text()='Technologies'])[1]")
        self.mobileApp=page.locator("//strong[text()='Mobile App Development']")
        self.react_native=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamarin_App=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter_mobile=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.ionic_app=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
    
    def mobileAppDevSubMenu(self):
        mobileAppList=[self.react_native,self.react_native,self.enterprise_mobile,self.xamarin_App, self.kotlin_mobile,self.flutter_mobile,self.ionic_app]
        for locator in mobileAppList:
            self.technologies.hover()
            self.page.wait_for_timeout(1000)
            self.mobileApp.hover()
            self.page.wait_for_timeout(1000)
            locator.click()
            self.page.wait_for_load_state(state="load")
            self.page.go_back()
            self.page.wait_for_load_state(state="load")