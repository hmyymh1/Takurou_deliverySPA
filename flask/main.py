from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_caching import Cache
import config
import hashlib,json,uuid

app = Flask(__name__)

app.config.from_object(config)

# 创建一个Mail类的实例
mail = Mail(app)

def send_mail(recipient,title,body):
    message = Message(title, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
    message.body = body
    mail.send(message)
    return "send mail"

# 创建cache实例
cache = Cache(app)

# 数据库配置
db = SQLAlchemy(app)

# 加密
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
# 定义User
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    mailaddress = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text)
    addressList = db.Column(db.JSON)
    orderLists = db.Column(db.JSON)

    def __init__(self, mailaddress, password):
        self.mailaddress = mailaddress
        self.password = get_md5(password)




"""
    接口说明：
    1.返回的是json数据
    2.结构如下
        {
            resCode:0 # 非0既错
            data:     # 数据位置，一般为数组
            message:  # '对本次请求的说明'
        }
"""
# 邮箱验证
@app.route('/mail_code', methods = ['POST'])
def mail_code():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        user_data = get_data['data']
        mailaddress = user_data['mailaddress']
        title = "認証コード"
        captcha = str(uuid.uuid1())[:6] #随机6位验证码
        body = "認証コード %s" %captcha

        # 修改邮箱时 验证邮箱是否存在
        if get_data['key'] == 'mailPass':
            loginUser = User.query.filter_by(mailaddress=mailaddress).first()
            if not loginUser:
                resData = {
                    'resCode': 1,
                    'data': [],
                    'message': '入力されたメールアドレスを認証できませんでした。',
                }
                return jsonify(resData)

        # 保存到redis数据库
        cache.set(mailaddress,captcha,timeout=60)

        send_mail(mailaddress,title,body)
        resData = {
            'resCode': 0,
            'data': [],
            'message': '送信しました',
        }
        return jsonify(resData)

# 邮箱修改
@app.route('/mail_pass',methods = ['POST'])
def mail_pass():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        user_data = get_data['data']
        mailaddress = user_data['mailaddress']
        password = user_data['password']
        code = user_data['code']
        loginUser = User.query.filter_by(mailaddress=mailaddress).first()
        if not mailaddress or not password:
            resData = {
                'resCode': 1,
                'data': [],
                'message': '信息不全',
            }
        elif not loginUser:
            resData = {
                'resCode': 1,
                'data': [],
                'message': '入力されたメールアドレスを認証できませんでした。',
            }
        elif not code or code != cache.get(mailaddress):
            resData = {
                'resCode': 1,
                'data': [],
                'message': '認証コードを正しく入力してください。',
            }
        else:
            loginUser.password = get_md5(password)
            db.session.commit()
            resData = {
                'resCode': 0,
                'data': [],
                'message': 'パスワード再設定しました',
            }
        return jsonify(resData)


# 注册
@app.route('/user_register',methods = ['POST'])
def user_register():
    if request.method == 'POST':
        print('捕获到了post请求')
        get_data = json.loads(request.get_data(as_text=True))
        user_data = get_data['data']
        mailaddress = user_data['mailaddress']
        password = user_data['password']
        code = user_data['code']
        loginUser = User.query.filter_by(mailaddress=mailaddress).first()
        if not mailaddress or not password:
            resData = {
                'resCode': 1,
                'data': [],
                'message': '信息不全',
            }
        elif loginUser:
            resData = {
                'resCode': 1,
                'data': [],
                'message': '入力されたメールアドレスは既に存在します',
            }
        elif not code or code != cache.get(mailaddress):
            resData = {
                'resCode': 1,
                'data': [],
                'message': '認証コードを正しく入力してください。',
            }
        else:
            user = User(mailaddress, password)
            db.session.add(user)
            db.session.commit()
            resData = {
                'resCode': 0,
                'data': [],
                'message': '登録しました',
            }
        return jsonify(resData)
    else:
        resData = {
            'resCode': 1,
            'data': [],
            'message': '请求方法错误',
        }
        return jsonify(resData)

# 增删地址
@app.route('/address_add',methods = ['POST'])
def address_add():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        addressList = get_data['data']
        mailaddress = get_data['key']
        loginUser = User.query.filter_by(mailaddress=mailaddress).first()
        loginUser.addressList = addressList
        db.session.commit()
        resData = {
            'resCode': 0,
            'data': [],
            'message': '地址修改成功',
        }
        return jsonify(resData)

# 获取用户数据
@app.route('/get_user_data',methods = ['POST'])
def get_user_data():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        mailaddress = get_data['key']
        loginUser = User.query.filter_by(mailaddress=mailaddress).first()
        resData = {
            'resCode': 0,
            'data': {
                'addressList': loginUser.addressList,
                'orderLists': loginUser.orderLists
            },
            'message': '获取用户数据',
        }
        return jsonify(resData)

# 登录
@app.route('/user_login',methods = ['POST'])
def user_login():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        user_data = get_data['data']
        mailaddress = user_data['mailaddress']
        password = user_data['password']
        loginUser = User.query.filter_by(mailaddress=mailaddress).first()
        if not mailaddress or not password:
            resData = {
                'resCode': 1,
                'data': [],
                'message': '入力されたメールアドレスとパスワードを認証できませんでした。',
            }
        elif not loginUser:
            resData = {
                'resCode': 1,
                'data': [],
                'message': '入力されたメールアドレスとパスワードを認証できませんでした。',
            }
        else:
            if loginUser.password != get_md5(password):
                resData = {
                    'resCode': 1,
                    'data': [],
                    'message': '入力されたメールアドレスとパスワードを認証できませんでした。',
                }
            else:
                resData = {
                    'resCode': 0,
                    'data': [],
                    'message': '登录成功',
                }
        return jsonify(resData)
    else:
        resData = {
            'resCode': 1,
            'data': [],
            'message': '请求方法错误',
        }
        return jsonify(resData)

# 订单
@app.route('/add_order',methods = ['POST'])
def add_order():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        order_data = get_data['data']
        mailaddress = get_data['key']
        orderList = order_data['orderList']
        loginUser = User.query.filter_by(mailaddress=mailaddress).first()
        if loginUser.orderLists is None:
            orderLists = []
            orderLists.append(orderList)
            loginUser.orderLists = orderLists
        else:
            orderLists = loginUser.orderLists
            orderLists.append(orderList)
            loginUser.orderLists = orderLists
        db.session.commit()
        # 发送邮件
        title = '【倬朗】ご注文を受付けました！'
        y = ''
        for item in orderList:
            y = y+item['item']['name']+' '+str(item['count'])+'個\n'
        body = 'ご注文ありがとうございます \n\n' \
               'お届け先情報\n' \
               'お名前:'+order_data['userAddress']['firstName']+order_data['userAddress']['givenName']+'\n' \
               '住所:'+order_data['userAddress']['fullAddress']+'\n' \
               '電話番号:'+order_data['userAddress']['tel']+'\n\n' \
               '注文商品\n'+y+'\n\n' \
               'ご請求金額合計:'+str(order_data['cartTotal'])+'円'
        send_mail(mailaddress,title,body)
        resData = {
            'resCode': 0,
            'data': [],
            'message': '订单添加',
        }
        return jsonify(resData)



@app.route('/',methods = ['GET','POST'])
def hello_world():
    return '111'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)