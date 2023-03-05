class BasePage:
    def __init__(self, browser, timeout=2):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        if self.browser.current_url == 'data:,':
            self.browser.get(url)
