import os


class Config:

   NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
   ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=402e289ced0e494ca62c66042f963a0c'
   NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
   SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
