# %%
import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/page/1/']


    def parse(self, response):

        for div in response.css('.quote'):
            quote = div.css('.text::text').get()
            author = div.css('.author::text').get()
            tags = div.css('.tags a::text').getall()
            yield {
                'quote':quote.replace('"','').replace('"','').replace(',',''),
                'author':author,
                'tags':tags
            }
        
        nextpageurl = response.css('li.next a::attr(href)').get()
        print(nextpageurl)
        if nextpageurl:
            yield response.follow(nextpageurl, callback=self.parse)
        