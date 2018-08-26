from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['get', 'post'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['get'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['post'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'zcx' and password == 'zcx':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='bad username or password', username=username)

if __name__ == '__main__':
    app.run()
