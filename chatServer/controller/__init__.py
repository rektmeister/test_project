from flask import Blueprint

user_blue = Blueprint('user', __name__, url_prefix='/api/v1/user')
friendly_blue = Blueprint('friendly', __name__, url_prefix='/api/v1/friendly')
news_blue = Blueprint('news', __name__, url_prefix='/api/v1/news')
sys_blue = Blueprint('sys', __name__, url_prefix='/api/v1/sys')
validate_blue = Blueprint('validate', __name__, url_prefix='/api/v1/validate')

from .user import user_blue
from .friendly import friendly_blue
from .news import news_blue
from .sys import sys_blue
from .validate import validate_blue

# 注册蓝图
def register_blueprint(app):
    # 用户模块
    app.register_blueprint(user_blue)
    app.register_blueprint(friendly_blue)
    app.register_blueprint(news_blue)
    app.register_blueprint(sys_blue)
    app.register_blueprint(validate_blue)
    return