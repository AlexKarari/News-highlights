class News_sources:
    '''
    News_sources class to define News_sources Objects
    '''

    def __init__(self, source_id, source_name, author, description, url):
        self.source_id = source_id
        source_name = source_name
        self.author = author
        self.description = description
        self.url = url
        
        

class News_articles:
    '''
    News_articles class to define News_articles Objects
    '''

    def __init__(self, source_id, source_name, author, title, description, urlToImage, url, publishedAt):
        self.source_id = source_id
        self.source_name = source_name 
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = "https://bloximages.chicago2.vip.townnews.com/host.madison.com/content/tncms/assets/v3/editorial/6/33/6339d38d-7b84-5eff-aeb3-8782281f7085/5ac81513bfd12.image.jpg?crop=1662%2C935%2C0%2C155&resize=1120%2C630&order=crop%2Cresize" + urlToImage
        self.url = url
        self.publishedAt = publishedAt


