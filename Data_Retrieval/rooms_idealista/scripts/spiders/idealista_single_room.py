# -*- coding: utf-8 -*-
import scrapy


class IdealistaSingleRoomSpider(scrapy.Spider):
    # name of spider
    name = 'idealista_single_room'
    # domains allowed to scrape
    allowed_domains = ['www.idealista.it']
    # url to scrape (always pay attention to the https protocol and eliminate the slash at the end of the site)
    # start_urls = ['https://www.glassesshop.com/bestsellers']
    # rotate_user_agent = True
    # this block overwrites the User Agent header (it is useful because I do not want to show that my User Agent is scrapy)
    def start_requests(self):
        yield scrapy.Request(url='https://www.idealista.it/affitto-stanze/roma-roma/', callback=self.parse, headers={
            "User-Agent":         
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    
        })

    # this block catches the response of the site above 
    def parse(self, response):
        for product in response.xpath("//div[@class='item-info-container']"):

            # this block returns a dictionary with features listed underneath
            yield {
                # START FROM THIS LINE 
                'room_address': product.xpath(".//a/text()").get(),
                'room_price': product.xpath(".//div/span/text()").get(), # this selects the room price
                'number_of_rooms': product.xpath(".//span[@class='item-detail'][1]/text()").get(), # this selects the number of rooms inside the apartment
                'number_of_people': product.xpath(".//span[@class='item-detail'][2]/text()").get(),
                # this line prints my User Agent 
                'user-agent': response.request.headers.get('User-Agent').decode('utf-8')
            }

        # this line selects the next page of the site
        string = "https://www.idealista.it"
        xpath = response.xpath("//a[@class='icon-arrow-right-after']/@href").get()
        next_page = string + xpath
       

        # if the next page exists than it executes the yield line
        if next_page:
            # it selects the next page url (if the next page does not exist then the next page will be none and it will not be called)
            # this line includes also the change for the User Agent so that I will not show that my user agant is scrapy
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
            })
