from flask_socketio import SocketIO
from flask import request
from flask_socketio import emit
import json
from .message import (
    m_sendNewMessage,
    m_goOnline,
    m_join,
    m_sendValidateMessage,
    m_sendAgreeFriendValidate,
    onLineUser,
    ComplexEncoder
)

socketio = SocketIO()


def init_socketio(app):
    socketio.init_app(app, cors_allowed_origins="*")
    return socketio


@socketio.on("connect")
def test_connect():
    print("socket 建立连接")


@socketio.on("sendNewMessage")
def sendNewMessage(data):
    m_sendNewMessage(data)


@socketio.on("goOnline")
def goOnline(data):
    m_goOnline(data)


@socketio.on("join")
def join(data):
    m_join(data)


@socketio.on("sendValidateMessage")
def sendValidateMessage(data):
    m_sendValidateMessage(data)


@socketio.on("sendAgreeFriendValidate")
def sendValidateMessage(data):
    m_sendAgreeFriendValidate(data)


@socketio.on("disconnect")
def handle_disconnect():
    # 用户断开连接时移除对应的在线用户并广播最新列表
    onLineUser.pop(request.sid, None)
    resJson = json.dumps(onLineUser, cls=ComplexEncoder)
    emit("onlineUser", resJson)