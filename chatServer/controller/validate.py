from controller import validate_blue
from model.validate_news import ValidateNews
from flask import request

# 获取验证码
@validate_blue.route("/myvalidatenews", methods=["GET"])
def myvalidatenews():
    id = int(request.args.get("id"))

    list = ValidateNews.query.filter(ValidateNews.reveiverId == id).all()

    resArr = []
    for item in list:
        resArr.append(dict(item))

    return {"status": 2000, "data": resArr, "msg": "获取数据成功！"}
