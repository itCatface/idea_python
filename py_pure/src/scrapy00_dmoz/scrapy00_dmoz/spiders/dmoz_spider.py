import src

from src.spider.scrapy00_dmoz.scrapy00_dmoz.items import DmozItem


class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["http://dmoztools.net"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open('../' + filename, 'wb') as f:
        #     f.write(response.body)

        # for sel in response.xpath('//ul/li'):
        #     title = sel.xpath('a/text()').extract()
        #     link = sel.xpath('a/@href').extract()
        #     desc = sel.xpath('text()').extract()
        #     print(title, link, desc)

        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
