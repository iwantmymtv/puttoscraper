import scrapy
from putto.items import PuttoItem
from putto.last import htmlstring
from selenium import webdriver
import time
import datetime


class PuttoScrape(scrapy.Spider):
	name = "putto"
	start_urls = ["https://bet.szerencsejatek.hu/jatekok/putto/sorsolasok/"]
	def __init__(self):
				self.driver = webdriver.Chrome()

	def parse(self,response):
		self.driver.get(response.url)
		while True:
			next = self.driver.find_element_by_xpath('//a[@class="prev-day"]')
			try:
					next.click()
					response1 =  scrapy.http.TextResponse(url=response.url, body=self.driver.page_source, encoding='utf-8')
					
					for i in response1.css('div.table-container tbody tr'):
						datestr = i.css('td:nth-child(1) div::text').get()
						dateobj = datetime.datetime.strptime(datestr, '%Y. %m. %d. %H:%M')
						date = dateobj
						betid = int(i.css('td:nth-child(2) div::text').get())
						nums = i.css('td:nth-child(3) div::text').get()
						n = nums.split(', ')
						Afield = [int(i) for i in n]
						Bfield = int(i.css('td:nth-child(4) div::text').get())
						yield PuttoItem(date=date,betid=betid,Afield=Afield,Bfield=Bfield)
			except:
						time.sleep(10)

		#self.driver.close()


				