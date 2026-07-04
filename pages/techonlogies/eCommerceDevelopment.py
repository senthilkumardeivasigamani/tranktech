class eCommerceDevelopment:
    def __init__(self,page):
        self.page=page
        self.technologies=page.locator("(//a[text()='Technologies'])[1]")
        self.ecomm=page.locator("//strong[text()='eCommerce Development']")
        self.magent_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.codeigniter_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.big_comm=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cs_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.open_cart=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.word_press=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.shopify_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.Node_Js=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.nop_comm=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.woo_Comm=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.laravel_Dev=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.prestashop_Dev=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.drupal_Dev=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.wix_Dev=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.joomla_Dev=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.react_JS_Dev=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.express_JS_Dev=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')

    def eCommerceDevelopmentSubMenu(self):
        eCommerceList=[self.magent_dev,self.codeigniter_dev,self.big_comm,self.cs_cart,self.open_cart,self.word_press,self.shopify_dev,self.Node_Js,self.nop_comm, self.woo_Comm,self.laravel_Dev,self.prestashop_Dev,self.drupal_Dev,self.wix_Dev,self.joomla_Dev,self.react_JS_Dev,self.express_JS_Dev]
        for locator in eCommerceList:
            self.technologies.hover()
            self.page.wait_for_timeout(1000)
            self.ecomm.hover()
            self.page.wait_for_timeout(1000)
            locator.click()
            self.page.wait_for_load_state(state="load")
            self.page.go_back()
            self.page.wait_for_load_state(state="load")