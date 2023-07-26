import scrapy

class AespaSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.ticketmaster.com.br/event/aespa']

    def parse(self, response):
        print(response.css, "\n\n\n\n\n\n")
        for title in response.css('.next'):
            yield {'title': title.css('::text').get()}

        # for next_page in response.css('a.next'):
        #     yield response.follow(next_page, self.parse)