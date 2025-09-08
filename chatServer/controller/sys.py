from controller import sys_blue
from model.sysuser import SysUser
from flask import request, send_file
import datetime

# 获取验证码
@sys_blue.route("/sysusers", methods=["GET"])
def sysusers():
    list = SysUser.query.filter().all()
    resArr = []
    for item in list:
        resArr.append(dict(item))
    return {"status": 2000, "data": resArr, "msg": "获取数据成功！"}


# 上传文件
@sys_blue.route("/upfile", methods=["POST"])
def upfile():
    file = request.files["file"]

    if file.filename == "":
        return {"status": 2001, "data": None, "msg": "未找到文件！"}

    arr = file.filename.split(".")
    time = str(datetime.datetime.now().timestamp()).replace(".", "") + "."
    fileName = arr[0] + "-" + time + arr[1]

    if file:
        file.save("uploads/" + fileName)
        return {"status": 2000, "data": fileName, "msg": "获取数据成功！"}
    
@sys_blue.route('/download')
def download():
    fileName = request.args.get("filename")
    return send_file('uploads/' + fileName, as_attachment=True)
