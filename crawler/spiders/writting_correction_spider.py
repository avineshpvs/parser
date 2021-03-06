# Spider that crawl the websites, download the raw html file
# and match the text error pattern
# Scrapy library is used because it is fast, asynchronous and can crawl thousands of websites efficiently
# https://doc.scrapy.org/en/latest/intro/install.html
import scrapy
import os
# from scrapy.selector import Selector

class WrittingTipSpider(scrapy.Spider):
    name = "writting_tips"
    # initial url list to parse
    def start_requests(self):
        urls = ['http://www.dailywritingtips.com/archives/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # callback for every request
    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = '%s.html' % page

        # if filename == 'archives.html':
        #     content = response.css('div.post').extract()
        # else:
        #     content = response.css('article.post').extract()
        #
        # if content is not None:
        #     with open(filename, 'w') as f:
        #         f.write(content[0])
        #     self.log('Saved file %s' % filename)
        # else:
        #     self.log('file %s is empty' % filename)

        links = response.css('div.post ul.postspermonth li a::attr(href)').extract()
        for l in links:
            if l is not None and l != "http://www.dailywritingtips.com/the-word-of-the-year-for-2016/":
                l = response.urljoin(l)
                yield scrapy.Request(l, callback=self.save_article)

            else:
                break

        print('done')


    def save_article(self, response):
        page = response.url.split("/")[-2]
        filename = 'data/%s.html' %  (page)

        content = response.css('article.post').extract()
        if content is not None:
            with open(filename, 'w') as f:
                f.write(content[0])
            self.log('Saved file %s' % filename)
        else:
            self.log('file %s is empty' % filename)
            # define pattern to match





