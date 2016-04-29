import re
from pprint import pprint
from scrapy import Request, Spider
from ..items import GetGoogleStoreCategoryItem as Item


def get_cat(s):
    ptn = re.compile(r".*?/category/([A-Z_]*).*")
    res = ptn.findall(s)
    if res:
        return res[0].lower()
    return ""


class GoogleStoreCatSpider(Spider):

    name = "google_cat"
    allowed_domains = ['play.google.com']

    def start_requests(self):
        temp = ("https://play.google.com/store/apps/categor"
                "y/BOOKS_AND_REFERENCE?hl=en&gl={gl}")
        url = temp.format(gl="us")
        headers = {
            'Referer': ('https://play.google.com/store/apps/ca'
                        'tegory/BOOKS_AND_REFERENCE?hl=en&gl=cw'),
        }
        yield Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        xpath = "//a[@class='child-submenu-link']/@href"
        res = response.xpath(xpath).extract()
        pprint(res)
        cats = [get_cat(ele) for ele in res]
        cats_set = set(cats)
        cats_set.remove("")
        for ele in cats_set:
            item = Item()
            item['cat'] = ele
            yield item
