from flask import render_template, url_for, flash, redirect, request
from Project_flask import app, db
from Project_flask.forms import RegistrationForm
from Project_flask.models import User
from flask_login import logout_user
from passlib.hash import sha256_crypt

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and sha256_crypt.verify(password, user.password):
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login')

@app.route("/edit_watched")
def edit_watched():
    return render_template('edit_watched.html')

@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

# @app.route("/edit_watched")
# def edit_watched():
#     return render_template('edit_watched.html')

@app.route("/add_movies")
def add_movies():
    return render_template('add_movies.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST":
        hashed_password = sha256_crypt.encrypt(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# @app.route('/get_started', methods=['POST'])
# def get_started():
#     username = request.form.get('username')
#     return redirect(url_for('login_page', username=username))

# @app.route('/get_started/<username>', methods=['GET', 'POST'])
# def login_page(username):
#     # Render the login page with the pre-filled username
#     return render_template('login.html', username=username)



# @app.route('/get_started', methods=['GET', 'POST'])
# def get_started():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         return redirect(url_for('login_page'))
#     else:
#         # Handle GET request or display an initial form
#         return render_template('get_started.html')

# @app.route('/get_started/<username>', methods=['POST'])
# def login_page(username):
#     # If you're using the parameter from the URL, you can remove the line below
#     # username = request.form.get('username')
#     return render_template('login.html', username=username)


# @app.route('/get_started', methods=['GET', 'POST'])
# def get_started():
#     if request.method == 'POST':
#         username = request.form['username']
#         return redirect(url_for('login_page', username=username))
#     else:
#         # Handle GET request or display an initial form
#         return render_template('homepage.html')

# @app.route('/get_started/<username>', methods=['GET','POST'])
# def login_page(username):
#     # If you're using the parameter from the URL, you can remove the line below
#     # username = request.form.get('username')
#     return render_template('login.html', username=username)

@app.route('/get_started', methods=['POST'])
def get_started():
    username = request.form.get('username')
    return render_template('login.html', username=username)


# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
#         if user and sha256_crypt.verify(password, user.password):
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('dashboard'))
#         else:
#             flash('Login Unsuccessful. Please check email and password', 'danger')
#     return render_template('login.html', title='Login')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))

