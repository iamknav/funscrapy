import scrapy

class BeebomSpider(scrapy.Spider):
    name = "beebom_spider"
    start_urls = [
        'https://beebom.com/category/tech/',
    ]
    
    def parse(self, response):
        for article in response.css("article"):
            yield {
                'title': article.css("h2 a::text").get(),
                'date': article.css("time::text").get(),
                'link': article.css("h2 a::attr(href)").get(),
                'excerpt': article.css("p.excerpt::text").get(),
            }
        
        next_page = response.css("a.next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
