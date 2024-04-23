from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Fixed admin username and password
admin_username = 'admin'
admin_password = 'adminpassword'

# Dummy user data for registration
users = {}


@app.route('/')
def home():
    return render_template("products.html")

@app.route('/login')
def loginpage():
    return redirect(url_for('login'))


@app.route('/loginpage', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username')
    password = request.form.get('password')

    if username == admin_username and password == admin_password:
        return redirect(url_for('dashboard', username=username)), 210
    elif username == admin_username and password != admin_password:
        return jsonify({'message': 'Incorrect admin password'}), 220
    elif username in users:
        if users[username] == password:
            return render_template('login_success.html', username=username), 200
        else:
            return jsonify({'message': 'Incorrect password. Please try again.'}), 406
    else:
        return jsonify({'message': 'Incorrect username. Please try again.', 'status_code': 404}), 404


@app.route('/register', methods=['POST','GET'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users:
        return jsonify({'message': 'Username already exists. Please choose a different username.', 'status_code': 400}), 400
    else:
        users[username] = password
        return jsonify({'message': 'You have been successfully registered! Please login.', 'status_code': 201}), 201


@app.route('/dashboard')
def dashboard():
    username = request.args.get('username')
    if username:
        return render_template('dashboard.html', username=username), 200
    else:
        return jsonify({'message': 'You need to login first.', 'status_code': 401}), 401


@app.route('/logout')
def logout():
    username = request.args.get('username')
    if username:
        return jsonify({'message': 'You have been logged out.', 'status_code': 200}), 200
    else:
        return jsonify({'message': 'You are not logged in.', 'status_code': 401}), 401


if __name__ == '__main__':
    app.run(debug=True)
