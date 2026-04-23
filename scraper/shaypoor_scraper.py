import time

class ShapoorScraper:
    def __init__(self, driver):
        self.driver = driver

    def load_page(self, url):
        self.driver.get(url)
    
    def get_ads(self):
        pass

    def scroll(self, times=5):
        for _ in range(times):
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(2)
