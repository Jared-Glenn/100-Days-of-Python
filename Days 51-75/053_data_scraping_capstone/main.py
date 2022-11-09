import zillow_scraper
import form_filler

zillow_scraper = zillow_scraper.ZillowScraper()


listing_list = zillow_scraper.get_data()
form_filler = form_filler.FormFiller(listing_list)

form_filler.fill_form()
