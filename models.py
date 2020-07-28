# coding=utf8

import datetime
import time
from sqlalchemy import Column, String, SmallInteger, Integer, BigInteger, UniqueConstraint, Index, Text, \
    Boolean

from database import Base


class BookMark(Base):
    """
    书签
    """
    domain = Column(String(100))
    base_url = Column(String(256))
    url = Column(String(512), unique=True)
    title = Column(String(128))
    image_url = Column(String(256))
    post_count = Column(Integer)
    hidden = Column(SmallInteger)

