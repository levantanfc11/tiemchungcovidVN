import scrapy
from..items import TiemchungItem
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrapy.utils.project import get_project_settings
import time as sleep

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
        
        settings= get_project_settings()
        driver_path = 'C:\VANTAN\Patch\chromedriver.exe'
        options= webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0, 3500)")
        click_button = driver.find_element_by_xpath('//div[@class="ng-star-inserted"]//button[@class="text-center btn btn-link"]')
        click_button.click()
        sleep(3)
        driver.close()

    def parse(self, response):
        for i in range(1, 63):
            tinh_thanhpho = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[2]//text()').get()
            dukien_vacxinphanbo = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[3]//text()').get()
            phanbo_thucte = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[4]//text()').get()
            dansodudieukientiemchung = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[5]//text()').get()    
            solieudatiemchung = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[6]//text()').get()
            tyledukiensetiemchung = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[7]//small[@class="d-flex w-100 clb"]//text()').get()
            tyledatiemchung = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[8]//small[@class="d-flex w-100 clb"]//text()').get()
            tyledatiemitnhatmotmui = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[9]//small[@class="d-flex w-100 clb"]//text()').get()
            tyledatiemchung_trenvacxinphanbothucte = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[10]//small[@class="d-flex w-100 clb"]//text()').get()
            tylephanbovacxin_trenvacxinphanbocanuoc = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[11]//small[@class="d-flex w-100 clb"]//text()').get()
            
            
            item = TiemchungItem()
            item['tinh_thanhpho'] = tinh_thanhpho
            item['dukien_vacxinphanbo'] = dukien_vacxinphanbo
            item['phanbo_thucte'] = phanbo_thucte
            item['dansodudieukientiemchung'] = dansodudieukientiemchung
            item['solieudatiemchung'] = solieudatiemchung
            item['tyledukiensetiemchung'] = tyledukiensetiemchung
            item['tyledatiemchung'] = tyledatiemchung
            item['tyledatiemitnhatmotmui'] = tyledatiemitnhatmotmui
            item['tyledatiemchung_trenvacxinphanbothucte'] = tyledatiemchung_trenvacxinphanbothucte
            item['tylephanbovacxin_trenvacxinphanbocanuoc'] = tylephanbovacxin_trenvacxinphanbocanuoc
            yield item
