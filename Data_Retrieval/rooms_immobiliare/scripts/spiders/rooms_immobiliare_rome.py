# -*- coding: utf-8 -*-
import scrapy


class RoomsImmobiliareRomeSpider(scrapy.Spider):
    name = 'rooms_immobiliare_rome'
    allowed_domains = ['www.immobiliare.it']
    # url to scrape (always pay attention to the https protocol and eliminate the slash at the end of the site)
    # start_urls = ['https://www.glassesshop.com/bestsellers']
    # rotate_user_agent = True
    # this block overwrites the User Agent header (it is useful because I do not want to show that my User Agent is scrapy)
    def start_requests(self):
        yield scrapy.Request(url='https://www.immobiliare.it/stanze/Roma/camere-Roma.html', callback=self.parse, headers={
            "User-Agent":         
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    
        })

    # this block catches the response of the site above 
    def parse(self, response):
        for product in response.xpath("//div[@class='listing-item_body--content']"):
            
            # this two lines serve to skip the rooms that have no price on the website
            room_price = product.xpath(".//ul/li[@class='lif__item lif__pricing']/text()").extract()
            a = room_price[0].strip() if room_price else ''

                # this block returns a dictionary with features listed underneath
            yield {
                'room_address': product.xpath(".//p/a/@title").get(), # this selects the room title and address
                'room_price': a,    # this selects the room price and the extract expression removes the \n character from the final output
                'number_of_rooms': product.xpath(".//ul/li[@class='lif__item'][1]/div/span/text()").extract_first(), # this selects the number of rooms inside the apartment
                # this line prints my User Agent 
                'user-agent': response.request.headers.get('User-Agent').decode('utf-8')
            }
                
        # this line selects the next page of the site
        # in this case I need to concatenate the first part of the site because when I click the 'next page' button on the site 
        # it is not explicitely mentioned the entire path
        string = "https://www.immobiliare.it/"
        xpath = response.xpath("//a[@title='Pagina successiva']/@href").get()
        next_page = string + xpath
       

        # if the next page exists than it executes the yield line
        if next_page:
            # it selects the next page url (if the next page does not exist then the next page will be none and it will not be called)
            # this line includes also the change for the User Agent so that I will not show that my user agant is scrapy
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
            })

