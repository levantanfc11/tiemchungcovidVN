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
            
            a_STTs = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[1]')
            b_citys = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[2]')
            c_dukien_vacxinphanbo = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[3]')
            d_phanbo_thucte = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[4]')
            e_dansodudieukientiemchung = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[5]')
            f_solieudatiemchung = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[6]')
            g_tyledukiensetiemchung = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[7]')
            h_tyledatiemchung = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[8]')
            p_tyledatiemitnhatmotmui = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[9]')
            s_tyledatiemchung_trenvacxinphanbothucte = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[10]')
            t_tylephanbovacxin_trenvacxinphanbocanuoc = driver.find_elements_by_xpath('//div[@class="col-lg-12 col-md-12 border-bound pt-3"]//app-local-vaccine-statistic//div//div//tbody//tr//td[11]')
            
                
            for i in range(0,63):
                # tyledukiensetiemchung = str(tyledukiensetiemchung)
                # if "%" in tyledukiensetiemchung:
                #     tyledukiensetiemchung = tyledukiensetiemchung.replace("%","")
                # tyledatiemchung = int(tyledatiemchung.rstrip("%"))
                item = Tiemchung1Item()
                item['a_STTs'] = a_STTs[i].text
                item['b_citys'] = b_citys[i].text
                item['c_dukien_vacxinphanbo'] = c_dukien_vacxinphanbo[i].text
                item['d_phanbo_thucte'] = d_phanbo_thucte[i].text
                item['e_dansodudieukientiemchung'] = e_dansodudieukientiemchung[i].text
                item['f_solieudatiemchung'] = f_solieudatiemchung[i].text
                item['g_tyledukiensetiemchung'] = g_tyledukiensetiemchung[i].text
                item['h_tyledatiemchung'] = h_tyledatiemchung[i].text
                item['p_tyledatiemitnhatmotmui'] = p_tyledatiemitnhatmotmui[i].text
                item['s_tyledatiemchung_trenvacxinphanbothucte'] = s_tyledatiemchung_trenvacxinphanbothucte[i].text
                item['t_tylephanbovacxin_trenvacxinphanbocanuoc'] = t_tylephanbovacxin_trenvacxinphanbocanuoc[i].text
                # "{},{},{},{},{},{},{},{},{},{},{}\n".format(item['STT'],item['tinh_thanhpho'],item['dukien_vacxinphanbo'],item['phanbo_thucte'],item['dansodudieukientiemchung'],item['solieudatiemchung'],item['tyledukiensetiemchung'],item['tyledatiemchung'],item['tyledatiemitnhatmotmui'],item['tyledatiemchung_trenvacxinphanbothucte'],item['tylephanbovacxin_trenvacxinphanbocanuoc'])
                yield item
    

        except:
            pass
        driver.quit()
