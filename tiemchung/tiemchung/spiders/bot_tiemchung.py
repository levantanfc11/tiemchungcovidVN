import scrapy
from..items import TiemchungItem
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from scrapy.utils.project import get_project_settings
import time as sleep


class BotTiemchungSpider(scrapy.Spider):
    name = 'bot_tiemchung'
    allowed_domains = ['https://tiemchungcovid19.gov.vn/portal']


    # def click_button(self):
    #     driver = webdriver.Chrome(executable_path='C:/VANTAN/Patch/chromedriver.exe')
    #     driver.get('https://tiemchungcovid19.gov.vn/portal')
    #     driver.execute_script("window.scrollTo(0, 3500)")
    #     click_button = driver.find_element_by_xpath('//div[@class="ng-star-inserted"]//button[@class="text-center btn btn-link"]')
    #     click_button.click()
    #     sleep(5)

        
    # def start_requests(self):
    #     # self.chrome =  webdriver.Chrome(executable_path='C:/VANTAN/Patch/chromedriver.exe')
    #     # self.chrome_options = Options()
    #     # self.chrome_options.add_argument("--headless")
    #     # self.chrome_options.add_argument('--no-sandbox')
    #     # self.chrome = webdriver.Chrome(executable_path='C:/VANTAN/Patch/chromedriver.exe', options=self.chrome_options)
    #     yield SeleniumRequest(
    #         url ="https://tiemchungcovid19.gov.vn/portal",
    #         wait_time = 3,
    #         screenshot = True,
    #         callback = self.parse, 
    #         dont_filter = True    
    #         )
        
    # def click_button(self, driver):
    #     driver = webdriver.Chrome(executable_path='C:/VANTAN/Patch/chromedriver.exe')
    #     # driver.get('https://tiemchungcovid19.gov.vn/portal')
    #     driver.execute_script("window.scrollTo(0, 3500)")
    #     click_button = driver.find_element_by_xpath('//div[@class="ng-star-inserted"]//button[@class="text-center btn btn-link"]')
    #     click_button.click()
    #     click_button = driver.find_element_by_xpath('/html/body/app-root/app-portal-layout/div/body/app-home/main/section/div/div[5]/div/app-local-vaccine-statistic/div/div[3]')
    #     click_button.click()
    #     sleep(10)
    def parse(self, response):
        # # self.chrome.get('https://tiemchungcovid19.gov.vn/portal')
        # # sleep(5)
        # xpath = '//*[@id="main"]/section/div/div[5]/div/app-local-vaccine-statistic/div/div[3]/button'
        # button = self.chrome.find_element_by_xpath(xpath)
        # button.click()
        # sleep(5)



        # for i in range(1, 63):
        #     tinh_thanhpho = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[2]//text()').get()
        #     dukien_vacxinphanbo = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[3]//text()').get()
        #     phanbo_thucte = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[4]//text()').get()
        #     dansodudieukientiemchung = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[5]//text()').get()    
        #     solieudatiemchung = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[6]//text()').get()
        #     tyledukiensetiemchung = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[7]//small[@class="d-flex w-100 clb"]//text()').get()
        #     tyledatiemchung = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[8]//small[@class="d-flex w-100 clb"]//text()').get()
        #     tyledatiemitnhatmotmui = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[9]//small[@class="d-flex w-100 clb"]//text()').get()
        #     tyledatiemchung_trenvacxinphanbothucte = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[10]//small[@class="d-flex w-100 clb"]//text()').get()
        #     tylephanbovacxin_trenvacxinphanbocanuoc = response.xpath(f'//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr[{i}]//td[11]//small[@class="d-flex w-100 clb"]//text()').get()
            
            
        #     item = TiemchungItem()
        #     item['tinh_thanhpho'] = tinh_thanhpho
        #     item['dukien_vacxinphanbo'] = dukien_vacxinphanbo
        #     item['phanbo_thucte'] = phanbo_thucte
        #     item['dansodudieukientiemchung'] = dansodudieukientiemchung
        #     item['solieudatiemchung'] = solieudatiemchung
        #     item['tyledukiensetiemchung'] = tyledukiensetiemchung
        #     item['tyledatiemchung'] = tyledatiemchung
        #     item['tyledatiemitnhatmotmui'] = tyledatiemitnhatmotmui
        #     item['tyledatiemchung_trenvacxinphanbothucte'] = tyledatiemchung_trenvacxinphanbothucte
        #     item['tylephanbovacxin_trenvacxinphanbocanuoc'] = tylephanbovacxin_trenvacxinphanbocanuoc
        #     yield item
        settings = get_project_settings()
        driver_path = settings.get('CHROME_DRIVER_PATH')
        options = webdriver.ChromeOptions()
        options.add_argument('disable-popup-blocking')
        options.add_argument('--log-level=1')
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
        # chrome =  webdriver.Chrome(executable_path='chromedriver.exe')
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--no-sandbox')
        # driver = webdriver.Chrome(executable_path='chromedriver.exe', options=self.chrome_options)
        driver.get('https://tiemchungcovid19.gov.vn/portal')
        tinh_thanhpho = driver.find_element_by_xpath('//*[@id="main"]/section/div/div[5]/div/app-local-vaccine-statistic/div/div[2]/table/tbody/tr[1]/td[2]')
        tinh_thanhpho = 'tan'
        item = TiemchungItem()
        item['tinh_thanhpho'] = tinh_thanhpho
        yield item
        


