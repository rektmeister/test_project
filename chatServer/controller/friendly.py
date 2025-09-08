from controller import friendly_blue
from flask import request
from model.friendly import Friendly
from model.user import User
from sqlalchemy import or_, and_


@friendly_blue.route("/recentconversation", methods=["POST"])
def recentconversation():
    recentFriendIds = request.json["recentFriendIds"]
    userId = request.json["userId"]

    a1 = None
    a2 = None

    # if len(recentFriendIds) > 0:
    #     a1 = and_(Friendly.user_y.in_(recentFriendIds), Friendly.user_m == userId)
    #     a2 = and_(Friendly.user_m.in_(recentFriendIds), Friendly.user_y == userId)
    # else:
    #     a1 = (Friendly.user_m == userId)
    #     a2 = (Friendly.user_y == userId)

    a1 = (Friendly.user_m == userId)
    a2 = (Friendly.user_y == userId)


    list = Friendly.query.filter(or_(a1, a2)).all()

    resList = []
    for item in list:
        resItem = {}
        resItem["_id"] = item._id
        resItem["userM"] = dict(User.query.filter(User._id == item.user_m).first())
        resItem["userY"] = dict(User.query.filter(User._id == item.user_y).first())

        resItem["userM"]["level"] = 0
        resItem["userY"]["level"] = 0
        resList.append(resItem)

    return {"status": 2000, "data": resList, "msg": "获取成功"}


@friendly_blue.route("/myfriends", methods=["GET"])
def myfriends():
    id = request.values["id"]

    mQuery = Friendly.query.filter(Friendly.user_m == id).all()
    yQuery = Friendly.query.filter(Friendly.user_y == id).all()

    data = []

    for item in mQuery:
        user = User.query.filter(User._id == item.user_y).first()
        data.append(
            {
                "createDate": item.create_date,
                "nickname": user.nickname,
                "photo": user.photo,
                "signature": user.signature,
                "_id": user._id,
                "level": 0,
                "roomid": id + "-" + str(user._id),
            }
        )

    for item in yQuery:
        user = User.query.filter(User._id == item.user_m).first()
        data.append(
            {
                "createDate": item.create_date,
                "nickname": user.nickname,
                "photo": user.photo,
                "signature": user.signature,
                "_id": user._id,
                "level": 0,
                "roomid": str(user._id) + "-" + id,
            }
        )

    return {"status": 2000, "data": data, "msg": "获取成功"}
