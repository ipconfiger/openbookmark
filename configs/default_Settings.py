# coding=utf8


class Config(object):
    """
    基本配置
    """
    DB_URI = 'postgresql+psycopg2://alex:@127.0.0.1/openbookmark'

    DOMAIN = ''

    DEBUG = True

    TIMEOUT = 3600

    REDIS_HOST = '127.0.0.1'

    REDIS_PORT = 6379