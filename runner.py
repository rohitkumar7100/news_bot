import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news_bot.spiders.news import  NewsSpider
import os


def scrap():
    clean_file()
    
    process= CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' ,
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'HeadLines_data.csv' 
        })
    process.crawl(NewsSpider)
    process.start()
    print("Scraping Completed...")
    
            
def clean_file():
    if os.path.exists("HeadLines_data.csv"):
        os.remove("HeadLines_data.csv")

# if __name__ == "__main__":
#     clean_file()
#     scrap()
