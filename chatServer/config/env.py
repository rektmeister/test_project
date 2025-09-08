import os

# 应用名称
import platform

FLASK_NAME = os.getenv("FLASK_NAME", "DEMO")
# 应用版本
FLASK_VERSION = os.getenv("FLASK_VERSION", "v2.2.0")
# 应用秘钥
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "d67beaf46fbf4f048d2eeb26fd62ea49")
# 应用运行地址
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
# 应用运行端口
FLASK_PORT = os.getenv("FLASK_PORT", 3333)
# 应用启动文件
FLASK_APP = os.getenv("FLASK_APP", "app.py")
# 应用环境变量
FLASK_ENV = os.getenv("FLASK_ENV", "development")
# 是否调试模式：是-True,否-False
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"
# 是否演示模式：是-True,否-False
FLASK_DEMO = os.getenv("FLASK_DEMO", "True") == "True"
# 系统环境:windows、linux
FLASK_SYSTEM = platform.system().lower()

# 应用根目录
FLASK_ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# 应用模板路径
FLASK_TEMPLATE_FOLDER = os.path.join(FLASK_ROOT_PATH, "/templates")
# 应用静态资源路径
FLASK_STATIC_FOLDER = os.path.join(FLASK_ROOT_PATH, "/static")
# 应用文件存储路径
FLASK_UPLOAD_DIR = os.getenv(
    "FLASK_UPLOAD_DIR", os.path.join(FLASK_ROOT_PATH, "/uploads")
)
# 正式图片路径
FLASK_IMAGE_PATH = FLASK_UPLOAD_DIR + "/images"
# 临时文件路径
FLASK_TEMP_PATH = FLASK_UPLOAD_DIR + "/temp"
# 应用图片域名
FLASK_IMAGE_URL = os.getenv("FLASK_IMAGE_URL", "")

# =============================================== 数据库配置 =================================================

# 数据库驱动
DB_DRIVER = os.getenv("DB_DRIVER", "mysql")
# 数据库地址
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
# 数据库端口
DB_PORT = os.getenv("DB_PORT", "3306")
# 数据库名称
DB_DATABASE = os.getenv("DB_DATABASE", "web_chat")
# 数据库账号
DB_USERNAME = os.getenv("DB_USERNAME", "root")
# 数据库密码
DB_PASSWORD = os.getenv("DB_PASSWORD", "0000")
# 数据表前缀
DB_PREFIX = os.getenv("DB_PREFIX", "flask_")
# 是否开启调试模式：是-True,否-False
DB_DEBUG = os.getenv("DB_DEBUG", "True") == "True"

# =============================================== 消息 =================================================
MESSAGE_SALT = os.getenv("salt", "bYDUSqEY")
