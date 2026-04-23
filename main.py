from scraper.driver import get_driver
from scraper.shaypoor_scraper import SheypoorScraper


driver = get_driver()
scraper = SheypoorScraper(driver)
scraper.load_page('https://www.sheypoor.com/s/babol/real-estate')
scraper.get_ads()

input('enter.....')
driver.quit()