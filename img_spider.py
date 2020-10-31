

import scrapy

class Bluespider(scrapy.Spider):
    
    name='img_spider'
    i=2
    #download_delay = 5.0
    start_urls={
        
        'https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?view=90&sort=1&scale=282'
       
         }
    def parse(self, response):
       # item=DownloadItem()
        images=response.xpath('//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li/a/meta/@content').getall()
        clean_image_urls=[]
        for img_url in images:
            clean_image_urls.append(response.urljoin(img_url))
         
        yield{
             'image_urls':clean_image_urls
             }
  
        next_page ='https://www.farfetch.com/in/shopping/men/shoes-2/items.aspx?page='+ str(Bluespider.i) +'&view=90&sort=4&scale=283'
        if Bluespider.i<=189:
             Bluespider.i+=1
             yield response.follow(next_page,callback=self.parse)
        
    