from controller import user_blue
from db import db
from flask import session, request
from model.user import User
import random
import string
from utils.user_util import create_hash_with_salt


# 获取验证码
@user_blue.route("/getcode", methods=["GET"])
def get_code():
    code = generate_numbers_code(4)
    session["code"] = code
    return {"data": code}


# 获取验证码
@user_blue.route("/prefetchuser", methods=["GET"])
def prefetchuser():
    type = request.args.get("type")
    q = request.args.get("q")
    page = int(request.args.get("page"))
    pageSize = int(request.args.get("pageSize"))

    pagination = (
        User.query.filter(User.name.like("%"+q+"%"))
        .order_by(User._id.desc())
        .paginate(page=page, per_page=pageSize, error_out=False)
    )
    queryData = pagination.items

    resArr = []
    for item in queryData:
        resArr.append(dict(item))

    return {"status": 2000, "data": resArr, "msg": "获取成功！"}


# 登录
@user_blue.route("/login", methods=["POST"])
def login():
    cvCode = request.json["cvCode"]
    password = request.json["password"]
    account = request.json["account"]

    if session["code"] != cvCode:
        return {
            "status": 1002,
            "data": None,
            "msg": "验证码错误",
        }

    user = User.query.filter(User.name == account).first()
    if user == None:
        return {
            "status": 1001,
            "data": None,
            "msg": "账号不存在或密码错误",
        }

    
    pwd = create_hash_with_salt(password, user.salt)
    session["salt"] = user.salt

    if user.password == pwd:
        userInfo = dict(user)
        return {
            "status": 1000,
            "data": userInfo,
            "msg": "登录成功",
        }
    else:
        return {
            "status": 1001,
            "data": None,
            "msg": "账号不存在或密码错误",
        }


# 注册
@user_blue.route("/register", methods=["POST"])
def register():
    data = request.json
    if session["code"] != data["cvCode"]:
        return {
            "status": 1002,
            "data": None,
            "msg": "验证码错误",
        }

    list = User.query.filter(User.name == data["account"]).all()

    if len(list) > 0:
        return {
            "status": 1003,
            "msg": "账号已存在",
        }

    salt = create_salt()

    pwd = create_hash_with_salt(data["password"], salt)

    user = User(status=0, name=data["account"], password=pwd, photo=data["avatar"], nickname = data["nickname"], salt = salt)

    db.session.add(user)
    db.session.commit()

    return {
        "status": 1005,
        "data": data["account"],
        "msg": "注册完成",
    }


# 定义一个函数来生成盐
def create_salt(length=8):
    return "".join(
        [random.choice(string.ascii_letters + string.digits) for _ in range(length)]
    )

# 生成验证码
def generate_numbers_code(length):
    # 生成由数字随机字符串
    characters = string.digits
    verification_code = "".join(random.choice(characters) for _ in range(length))
    return verification_code
