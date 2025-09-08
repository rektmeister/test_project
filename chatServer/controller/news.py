from controller import news_blue
from flask import request
from model.news import News
from db import db
from utils.rsa_util import rsa_encrypt

@news_blue.route("/last", methods=["POST"])
def get_code():
    roomid = request.json["roomid"]
    list = News.query.filter(News.roomid == roomid).order_by(News._id.desc()).all()

    data = {}
    if len(list) > 0:
        data = dict(list[0])
        if data["isReadUser"] != None:
            data["isReadUser"] = data["isReadUser"].split(",")
        else:
            data["isReadUser"] = []

        data["message"] = rsa_encrypt(data["message"])

        data["time"] = data["time"].strftime("%Y-%m-%d %H:%M:%S")

    return {"status": 2000, "data": data, "msg": "获取成功"}


@news_blue.route("/isread", methods=["POST"])
def isread():
    roomid = request.json["roomid"]
    userId = request.json["userId"]

    news = News.query.filter(News.roomid == roomid).order_by(News._id.desc()).first()
    if news != None:
        if news.isReadUser != None:
            arr = news.isReadUser.split(",")
            if str(userId) not in arr:
                arr.append(str(userId))
                news.isReadUser = ",".join(arr)
        else:
            news.isReadUser = str(userId)

    db.session.commit()

    return {"status": 2000, "data": None, "msg": "success"}


@news_blue.route("/recent", methods=["GET"])
def recent():
    roomid = request.values["roomid"]
    page = int(request.values["page"])
    pageSize = int(request.values["pageSize"])

    pagination = (
        News.query.filter(News.roomid == roomid)
        .order_by(News._id.desc())
        .paginate(page=page, per_page=pageSize, error_out=False)
    )
    queryData = pagination.items
    
    res = []

    for item in queryData:
        data = dict(item)
        if data["isReadUser"] != None:
            data["isReadUser"] = data["isReadUser"].split(",")
        else:
            data["isReadUser"] = []

        data["time"] = data["time"].strftime("%Y-%m-%d %H:%M:%S")
        data["message"] = rsa_encrypt(data["message"])
        res.append(data)

    return {"status": 2000, "data": res, "msg": "获取成功"}
