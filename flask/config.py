import os

# 开启secret_key
SECRET_KEY = os.urandom(24)

# 开启debug模式, 需要在pycharm的Edit Configurations中勾选FLASK_DEBUG
DEBUG = False

# 配置数据库
MYSQL_HOST = '124.156.239.46'
MYSQL_PORT = 3306
MYSQL_USERNAME = 'demae'
MYSQL_PASSWORD = 'x8n3fKsAEwtarN8S'
MYSQL_DATABASE = 'demae'
MYSQL_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}".format(
    username=MYSQL_USERNAME,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    database=MYSQL_DATABASE
)

SQLALCHEMY_DATABASE_URI = MYSQL_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 配置邮箱
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'takurou.help@gmail.com'
MAIL_PASSWORD = 'A123456!'

# Redis数据库配置
CACHE_TYPE = 'redis'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_POST = 6379
CACHE_REDIS_DB = ''
CACHE_REDIS_PASSWORD = ''