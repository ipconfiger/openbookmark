# coding=utf8

from .default_Settings import Config
from .config import ProdConfig

__all__ = ['settings']


def load_settings():
    configObject = Config()

    print('url:%s' % configObject.DB_URI)
    for attr_name in dir(ProdConfig):

        if not attr_name.startswith('_'):
            print('process:%s' % attr_name)
            if hasattr(Config, attr_name):
                setattr(configObject, attr_name, getattr(ProdConfig, attr_name))
            else:
                setattr(configObject, attr_name, getattr(Config, attr_name))

    return configObject


settings = load_settings()
print(settings)