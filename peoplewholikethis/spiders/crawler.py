import scrapy

class TextSpider(scrapy.Spider):
  name="text"

  def start_requests(self):

    #tell it which website(s) to visit
    # urls=[
    #   'http://books.toscrape.com']
    urls = ["https://www.amazon.com/Electric-Toothbrush-Replacement-Inductive-Environmental/product-reviews/B07WQVVHXW/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber=3"]
    #visit each url
    for url in urls:

      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    #set a filename to write the response to
    # filename = 'books.html'
    # with open(filename, 'wb') as f:
    #   f.write(response.body)
      #as we can see in the page’s HTML, each book is contained in an <article> with the class ‘product_pod’, so we’ll tell Scrapy to start there
    # from scrapy.shell import inspect_response
    # inspect_response(response, self)
    # print("Using x path")
    # x_path ="/html/body/div[1]/div[3]/div[1]/div[1]/div/div[1]/div[5]/div[3]/div/div[2]/div/div/div[1]/a/div[2]/span"
    # for sel in response.xpath(x_path):
    #     print(sel)
    #     # title = sel.xpath('a/text()').extract()
    #     # link = sel.xpath('a/@href').extract()
    #     # desc = sel.xpath('text()').extract()
    #     # print title, link, desc
    print("Got results")
    for response in response.xpath('//span[@class = "a-profile-name"]/text()'):
        print(response.extract())
        yield {"title": str(response.extract())}

    # for book in response.css("a-profile-name"):
    #     print(book)
    #     yield {
    #       "title": book.css("span").extract()
    #     }


    # self.log('Saved file %s' % filename)