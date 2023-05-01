# %%
import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/']


    def parse(self, response):
        for tr in response.css('.titleColumn'):
            movieName = tr.css('a::text').get()
            year = tr.css('.secondaryInfo::text').get()
            movieurl = tr.css('a::attr(href)').get()
            #print(movieurl, year,movieurl)
            yield response.follow(movieurl,callback=self.paerseInfo)
            # yield{
            #     'title': title,
            #     'year':year
            # }
    def paerseInfo(self,response):
        print(response.url)
