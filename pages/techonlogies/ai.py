class ai:
    def __init__(self, page):
        self.page = page
        self.technologies = page.locator("(//a[text()='Technologies'])[1]")
        self.ai = page.locator("//strong[text()='Artificial Intelligence']")
    
    def aiSubMenu(self):
        self.technologies.hover()
        self.page.wait_for_timeout(1000)
        self.ai.click()
        self.page.go_back()
        self.page.wait_for_load_state(state="load")