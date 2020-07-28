# coding=utf8
from fastapi import FastAPI, Depends, Response, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from configs import settings
from service import BaseResponse
from bookmarks.services import BookmarkService, BookMarkResponse, BookMarkForm, BookmarkListResponse

app = FastAPI()

security = HTTPBasic()


def error_response(rep: Response, code: int, info: str):
    rep.status_code = code
    return BaseResponse(rs=False, code=code, info=info)


@app.get("/")
def site_root():
    """
    网站首页
    :return:
    """
    return {"it works"}


@app.post('/mark', response_model=BookMarkResponse)
def post_new_bookmark(form: BookMarkForm):
    """
    提交一个书签
    """
    bookmarkService = BookmarkService.appendNew(form.title, form.url, form.imageUrl)
    return bookmarkService.make_response()


@app.get('/mark', response_model=BookmarkListResponse)
def fetch_many_bookmarks():
    """
    获取书签列表
    """
    return BookmarkService.fetchMany()
