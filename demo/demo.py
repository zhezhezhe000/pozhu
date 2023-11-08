from flask import Flask, render_template, request, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置密钥


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # 在此处进行身份验证逻辑，验证用户名和密码是否正确
    # 这里只做简单的示例验证，实际应用中应使用更安全的验证方式
    if username == 'admin' and password == 'password':
        # 登录成功，设置 Cookie
        response = make_response('Login successful!')
        response.set_cookie('username', username)
        return response

    # 登录失败，重定向到登录页面
    return render_template('login.html', error=f'{username}-{password}:Invalid username or password')


@app.route('/admin')
def admin():
    # 检查 Cookie 中的用户名
    username = request.cookies.get('username')
    if username == 'admin':
        return 'Welcome to the admin page!'
    else:
        return 'Unauthorized!'


if __name__ == '__main__':
    app.run()
    # app.run(host="0.0.0.0",port=5000)