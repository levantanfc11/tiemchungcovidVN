import scrapy
from..items import TiemchungItem
from scrapy_selenium import SeleniumRequest


class BotTiemchungSpider(scrapy.Spider):
    name = 'bot_tiemchung'
   
    def start_requests(self):
        yield SeleniumRequest(
            url ="https://tiemchungcovid19.gov.vn/portal",
            wait_time = 3,
            screenshot = True,
            callback = self.parse, 
            dont_filter = True    
        )


    def parse(self, response):
        name_city = response.xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div/div//tbody//tr//td[2]//text()').get()
        item = TiemchungItem()
        item['name_city'] = name_city
        yield item
