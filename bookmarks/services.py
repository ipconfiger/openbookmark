# coding=utf8
import random
import time
from typing import List
from service import BaseService, BaseResponse
from models import BookMark
from pydantic import BaseModel, Field
from database import insert, delete, commit
__author__ = 'Alexander.Li'


class BookMarkForm(BaseModel):
    title: str = Field('', title=u"网页标题", max_length=128)
    url: str = Field('', title=u"网址", max_length=512)
    imageUrl: str = Field('', title=u"图片地址", max_length=256)


class BookmarkMode(BaseModel):
    domain: str = Field(None, title=u"域名")
    url: str = Field(None, title=u"网址")
    title: str = Field(None, title=u"网页标题")
    imageUrl: str = Field(None, title=u"图片地址")
    postCount: int = Field(None, title=u"提交次数")


class BookMarkResponse(BaseResponse):
    bookmark: BookmarkMode = Field('', title=u'书签对象')


class BookmarkListResponse(BaseResponse):
    bookmarks: List[BookmarkMode] = Field('', title=u"书签列表")


class BookmarkService(BaseService):
    """
    Bookmark的服务模块
    """

    def withId(self, bookMarkId: int) -> 'BookmarkService':
        self._id = bookMarkId
        return self

    def toResponse(self, bookmark):
        return BookmarkMode(
                domain=bookmark.domain,
                url=bookmark.url,
                title=bookmark.title,
                imageUrl=bookmark.image_url,
                postCount=bookmark.post_count
        )

    def make_response(self):
        bookmark = BookMark.filter(BookMark.id == self._id).first()
        return BookMarkResponse(
            bookmark=self.toResponse(bookmark)
        )

    @classmethod
    def appendNew(cls, title: str, url: str, image_url: str) -> 'BookmarkService':
        """
        添加新的书签
        """
        no_slash_url = url.split("#")[0]
        base_url = no_slash_url.split('?')[0]
        domain = no_slash_url.split('/')[2]
        bookmark = BookMark.filter(BookMark.url == no_slash_url).first()
        if not bookmark:
            bookmark = BookMark(domain=domain, title=title, base_url=base_url, url=no_slash_url, image_url=image_url,
                                post_count=1, hidden=0)
            insert(bookmark)
        else:
            bookmark.post_count+=1
        commit()
        return BookmarkService().withId(bookmark.id)

    @classmethod
    def fetchMany(cls):
        """
        随机取一堆
        """
        bookmarks = BookMark.filter(BookMark.hidden < 1).order_by(BookMark.id.desc())[:20]
        this = cls()
        return BookmarkListResponse(
            bookmarks=[this.toResponse(bookmark) for bookmark in bookmarks]
        )
