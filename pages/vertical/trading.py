class trading:
    def __init__(self,page):
        self.page=page
        self.verticals=page.locator("(//a[text()='Verticals'])[1]")
        self.trading=page.locator("//strong[text()='Trading']")
        self.ret_ecomm=page.locator("//strong[text()='Retail and Ecommerce']")
        self.healthcare=page.locator("//strong[text()='Healthcare']")
        self.fintech=page.locator("//strong[text()='Fintech']")
        self.custom_App=page.locator("//strong[text()='Custom App']")

        #trading
        self.stock_trad=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.anlog_trade=page.locator("//a[text()='Algo Trading']")
        self.paper_trade=page.locator("//a[text()='Paper Trading']")
        self.custom_trade=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.cfd_trade=page.locator("(//a[text()='CFD Trading'])[1]")
        self.web_trade=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.tradeapp=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')

    def mouseHover(self):
        list1=[self.trading,self.ret_ecomm,self.healthcare,self.fintech,self.custom_App]
        for locator in list1:
            self.verticals.hover()
            locator.hover()
            self.page.wait_for_timeout(2000)

    def tradingSubMenu(self):
        tradingList=[self.stock_trad,self.anlog_trade,self.paper_trade,self.custom_trade,self.cfd_trade,self.web_trade,self.tradeapp]
        for locator in tradingList:
            self.verticals.hover()
            self.page.wait_for_timeout(500)
            self.trading.hover()
            self.page.wait_for_timeout(500)
            locator.click()
            self.page.wait_for_timeout(500)
            self.page.go_back()
