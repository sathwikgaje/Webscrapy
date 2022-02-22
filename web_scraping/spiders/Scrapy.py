import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'Scrapy'
    start_urls = ['https://in.seamsfriendly.com/collections/shorts']

    def parse(self, response):
        for products in response.css('div.boost-pfs-filter-products ProductList ProductList--grid ProductList--removeMargin Grid'):
            yield {
            'Title': products.css('h2.ProductItem__Title Heading::text').get() ,
            'Prices': products.css('span.ProductItem__Price Price Text--subdued::text').get(),
            'Image urls':products.css('img.ProductItem__Image ProductItem__Image--alternate').attrib('src'),
            }