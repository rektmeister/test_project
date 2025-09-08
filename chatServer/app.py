from flask import Flask
from urllib.parse import quote_plus as urlquote
from config.env import (
    FLASK_HOST,
    FLASK_PORT,
    FLASK_DEBUG,
    DB_HOST,
    DB_PORT,
    DB_DATABASE,
    DB_USERNAME,
    DB_PASSWORD,
)
from controller import register_blueprint
from socketapp import init_socketio
from db import init_db


# 创建应用APP
def create_app():
    app = Flask(__name__, instance_relative_config=True,static_folder='uploads', static_url_path='/')

    # 注册蓝图到
    register_blueprint(app)

    # 应用配置
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql://"
        + DB_USERNAME
        + ":"
        + urlquote(DB_PASSWORD)
        + "@"
        + DB_HOST
        + ":"
        + DB_PORT
        + "/"
        + DB_DATABASE
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True

    app.config["SECRET_KEY"] = "I am a key!"

    # # 初始化扩展
    # register_extends(app)
    # # 注册中间件
    # register_middleware(app)

    # 返回APP
    return app


# 创建应用实例
app = create_app()
socketio = init_socketio(app)
db = init_db(app)

if __name__ == "__main__":
    # app.run()
    # 启动应用
    try:
        socketio.run(app=app, host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
    finally:
        print()
