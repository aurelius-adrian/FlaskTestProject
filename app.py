import secrets
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route('/')
def home():
    return render_template('login.html', data="Enter Credentials")


def refresh():
    if session.get('logged_in'):
        return render_template('input.html')
    else:
        return render_template('login.html', data="Incorrect Credentials")


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        flash('correct pwd')
        return refresh()
    else:
        session['logged_in'] = False
        flash('wrong password!')
        return refresh()


@app.route('/input', methods=['POST'])
def do_input():
    data = request.form['query']
    return render_template('input.html', data=data)


if __name__ == "__main__":
    # app.config['SESSION_TYPE'] = 'filesystem'
    # sess = Session()
    # sess.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=4000)
