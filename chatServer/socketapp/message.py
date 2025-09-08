from model.news import News
from db import db
from flask_socketio import emit, join_room
from flask import request
import datetime
import json
from utils.complexEncoder import ComplexEncoder
from model.validate_news import ValidateNews
from model.friendly import Friendly
from utils.rsa_util import rsa_decrypt,rsa_encrypt


onLineUser = {}
conversationList = {}

def m_sendNewMessage(data):
    if data["conversationType"] == "FRIEND":
        now = datetime.datetime.fromtimestamp(data["time"] / 1000)

        data["message"] = rsa_decrypt(data["message"])

        news = News(
            roomid=data["roomid"],
            senderId=data["senderId"],
            time=now,
            message=data["message"],
            messageType=data["messageType"],
        )

    del data["conversationType"]

    db.session.add(news)
    db.session.commit()
    data["_id"] = news._id

    data["message"] = rsa_encrypt(data["message"])

    emit("receiveMessage", data, to=data["roomid"])


def m_goOnline(data):
    if data == None:
        return

    # Remove existing entries for the same user
    for sid, info in list(onLineUser.items()):
        if info["_id"] == data["_id"]:
            del onLineUser[sid]

    onLineUser[request.sid] = {
        "_id": data["_id"],
        "name": data["name"],
        "nickname": data["nickname"],
        "loginTime": datetime.datetime.now(),
    }

    resJson = json.dumps(onLineUser, cls=ComplexEncoder)
    emit("onlineUser", resJson)


def m_join(data):
    roomid = data["roomid"]
    join_room(roomid)
    conversationList[roomid] = request.sid
    emit("conversationList", conversationList, to=roomid)


def m_sendValidateMessage(data):
    list = ValidateNews.query.filter(
        ValidateNews.status == 0, ValidateNews.senderId == data["senderId"], ValidateNews.reveiverId == data["reveiverId"]
    ).all()

    if len(list) == 0:
        news = ValidateNews(
            roomid=data["roomid"],
            senderId=data["senderId"],
            senderAvatar=data["senderAvatar"],
            senderName=data["senderName"],
            senderNickname=data["senderNickname"],
            status=data["status"],
            validateType=data["validateType"],
            time=data["time"],
            additionMessage=data["additionMessage"],
            reveiverId=data["reveiverId"],
        )
        db.session.add(news)
        db.session.commit()
        emit("receiveValidateMessage", dict(news), to=data["roomid"])


def m_sendAgreeFriendValidate(data):
    friendly = Friendly(
        user_m=data["senderId"],
        user_y=data["reveiverId"],
        create_date=datetime.datetime.now(),
    )

    db.session.add(friendly)

    roomid = data["roomid"]
    reveiverId = data["reveiverId"]
    senderId = data["senderId"]
    #senderRoomId = roomid.replace(str(reveiverId), str(senderId))

    data["add"] = False

    #emit("receiveValidateMessage", data, to=senderRoomId)
    emit("receiveValidateMessage", data, to=roomid)

    validateNews = ValidateNews.query.filter(
        ValidateNews.roomid == roomid,
        ValidateNews.reveiverId == reveiverId,
        ValidateNews.senderId == senderId,
    ).first()

    validateNews.status = 1
    db.session.commit()
