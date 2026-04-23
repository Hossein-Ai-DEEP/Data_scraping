from time import sleep
from scraper.utils import human_sleep
import random
import os
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SheypoorScraper:
    def __init__(self, driver):
        self.driver = driver
        self.visited = set()
        self.output_file = "sheypoor_ads.csv"

        if not os.path.exists(self.output_file):
            with open(self.output_file,'w', newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                                    "url",
                                    "title",
                                    "total_price",
                                    "price_per_meter",
                                    "area",
                                    "rooms",
                                    "parking",
                                    "storage",
                                    "elevator",
                                    "building_age",
                                    "location",
                                    "description"
                                ])


    def load_page(self, url):
        self.driver.get(url)
    
    def get_ads(self):
        try:
            cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, 'a.flex.h-auto')
                )
            )
        except:
            print("------------ NO ADS (TIMEOUT) ------------")
            return False

        print(f"Found {len(cards)} ads.")

        first_ad = cards[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", 
            first_ad
        )
        sleep(1)
        self.driver.execute_script("arguments[0].click();", first_ad)

        print("Ad clicked.")
        return True
    

    def human_scroll(self):
        scroll_amount = random.randint(700, 1400)
        self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        human_sleep(2.5, 5.5)
