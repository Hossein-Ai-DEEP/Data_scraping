from scraper.driver import get_driver
from scraper.shaypoor_scraper import ShapoorScraper


driver = get_driver()
scraper = ShapoorScraper(driver)
scraper.load_page('https://www.sheypoor.com/s/babol/real-estate')
scraper.scroll(3)

input('enter.....')
driver.quit()