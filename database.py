# coding=utf8

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, BigInteger
from configs import settings

engine = create_engine(settings.DB_URI, convert_unicode=True, client_encoding="utf8")
Session = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=True,
                                 bind=engine))

class DeclaredBase(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    def as_dict(self):
        """
        格式化成字典
        :return:
        :rtype:
        """
        result_dict = {}
        mapper = inspect(self.__class__)
        for column in mapper.attrs:
            name = column.key
            value = getattr(self, name)
            result_dict[name] = value if value is not None else ''
        return result_dict

    def as_json_dict(self):
        """
        返回可以通过jsonify格式化的字典(处理了datetime和Decimal类型)
        :return:
        :rtype:
        """
        import datetime
        from decimal import Decimal
        result_dict = self.as_dict()
        for property_name in result_dict:
            if isinstance(result_dict [property_name], datetime.datetime):
                result_dict[property_name] = result_dict[property_name].strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(result_dict[property_name], datetime.date):
                result_dict[property_name] = result_dict[property_name].strftime('%Y-%m-%d')
            elif isinstance(result_dict[property_name], Decimal):
                result_dict[property_name] = float(result_dict[property_name])
        return result_dict

    @classmethod
    def byId(cls, instance_id):
        """
        通过ID获取记录
        :param instance_id:
        :type instance_id:
        :return:
        :rtype:
        """
        return cls.query.get(instance_id)

    @classmethod
    def filter(cls, *conditions):
        return cls.query.filter(*conditions)


def insert(*instanceArr):
    for ins in instanceArr:
        Session.add(ins)
    Session.flush()


def delete(*instanceArr):
    for ins in instanceArr:
        Session.delete(ins)
    Session.flush()


def commit():
    Session.commit()


def rollback():
    Session.rollback()


Base = declarative_base(cls=DeclaredBase)
Base.query = Session.query_property()
