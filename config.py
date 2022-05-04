class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = '28488a3d739358a72809bafba00b9bb0'
    SECRET_KEY = 'catherinekimani'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wambui@localhost/watchlist'

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}