from flask import Flask, render_template, request, make_response
from captcha.image import ImageCaptcha
import random
import base64

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 验证码图片生成器
captcha = ImageCaptcha()

# 生成一个随机验证码字符串
def generate_captcha():
    captcha_text = ''.join(random.choice('0123456789') for _ in range(4))
    return captcha_text

@app.route('/')
def index():
    # 生成验证码并将其保存到 Flask 会话中
    captcha_text = generate_captcha()
    app.captcha_text = captcha_text
    data = captcha.generate(captcha_text)

    # 对验证码图像数据进行 base64 编码
    captcha_base64 = base64.b64encode(data.getvalue()).decode('utf-8')

    return render_template('login1.html', captcha=captcha_base64)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    entered_captcha = request.form.get('captcha')

    # 验证验证码
    if entered_captcha != app.captcha_text:
        return render_template('login1.html', error='Invalid captcha')

    # 在此处进行身份验证逻辑，验证用户名和密码是否正确
    if username == 'admin' and password == 'password':
        response = make_response('Login successful!')
        response.set_cookie('username', username)
        return response

    return render_template('login1.html', error='Invalid username or password')

@app.route('/admin')
def admin():
    username = request.cookies.get('username')
    if username == 'admin':
        return 'Welcome to the admin page!'
    else:
        return 'Unauthorized!'

if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0",port=5000)