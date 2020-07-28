# coding=utf8
from database import Base
from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    rs: bool = Field(True, title=u"业务逻辑执行结果")
    code: int = Field(200, title=u"返回结果编码，默认200是正确")
    info: str = Field('', title=u"如果错误的时候返回错误信息")


class BaseService(object):
    def __init__(self):
        self._id = 0
        self._ins = None

    def ofId(self, _id: int, _type: Base):
        self._id = _id
        self._ins = Base.byId(_id)
        return self

    def ofInstance(self, _ins: object):
        self._ins = _ins
        self._id = _ins.id
        return self





