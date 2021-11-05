import scrapy
from ..items import Tiemchung1Item
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from scrapy.utils.project import get_project_settings
import time

class BotTiemchung1Spider(scrapy.Spider):
    name = 'bot_tiemchung1'
    allowed_domains = ['tiemchungcovid19.gov.vn']
    start_urls = ['http://tiemchungcovid19.gov.vn/']

    def parse(self, response):
        settings = get_project_settings()
        driver_path = settings.get('CHROME_DRIVER_PATH')
        options = webdriver.ChromeOptions()
        options.add_argument('disable-popup-blocking')
        options.add_argument('--log-level=1')
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
        driver.get('http://tiemchungcovid19.gov.vn/')
        try:
            driver.maximize_window()
            driver.execute_script("window.scrollTo(0, 3500)")
            click_button = driver.find_element_by_xpath('//div[@class="ng-star-inserted"]//button[@class="text-center btn btn-link"]')
            time.sleep(5)
            click_button.click()
            
            STTs = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[1]')
            tinh_thanhpho = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[2]')
            dukien_vacxinphanbo = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[3]')
            phanbo_thucte = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[4]')
            dansodudieukientiemchung = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[5]')
            solieudatiemchung = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[6]')
            tyledukiensetiemchung = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[7]')
            tyledatiemchung = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[8]')
            tyledatiemitnhatmotmui = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[9]')
            tyledatiemchung_trenvacxinphanbothucte = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[10]')
            tylephanbovacxin_trenvacxinphanbocanuoc = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[11]')
            for i in range(0,63):
                item = Tiemchung1Item()
                item['STT'] = STTs[i].text
                item['tinh_thanhpho'] = tinh_thanhpho[i].text
                item['dukien_vacxinphanbo'] = dukien_vacxinphanbo[i].text
                item['phanbo_thucte'] = phanbo_thucte[i].text
                item['dansodudieukientiemchung'] = dansodudieukientiemchung[i].text
                item['solieudatiemchung'] = solieudatiemchung[i].text
                item['tyledukiensetiemchung'] = tyledukiensetiemchung[i].text
                item['tyledatiemchung'] = tyledatiemchung[i].text
                item['tyledatiemitnhatmotmui'] = tyledatiemitnhatmotmui[i].text
                item['tyledatiemchung_trenvacxinphanbothucte'] = tyledatiemchung_trenvacxinphanbothucte[i].text
                item['tylephanbovacxin_trenvacxinphanbocanuoc'] = tylephanbovacxin_trenvacxinphanbocanuoc[i].text
                # "{},{},{},{},{},{},{},{},{},{},{}\n".format(item['STT'],item['tinh_thanhpho'],item['dukien_vacxinphanbo'],item['phanbo_thucte'],item['dansodudieukientiemchung'],item['solieudatiemchung'],item['tyledukiensetiemchung'],item['tyledatiemchung'],item['tyledatiemitnhatmotmui'],item['tyledatiemchung_trenvacxinphanbothucte'],item['tylephanbovacxin_trenvacxinphanbocanuoc'])
                yield item
    

        except:
            pass
        driver.quit()
