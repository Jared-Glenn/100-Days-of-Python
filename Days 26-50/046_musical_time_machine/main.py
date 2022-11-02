import web_scraper
import playlist_maker

web_scraper = web_scraper.WebScraper()
song_list = web_scraper.get_songs()

playlist_maker = playlist_maker.PlaylistMaker(song_list)
playlist_maker.create_playlist(web_scraper.date)
playlist_maker.search_songs()
playlist_maker.add_songs()
