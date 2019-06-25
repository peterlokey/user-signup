from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route('/')
def index():
    username_error = request.args.get('username_error')
    password_error = request.args.get('password_error')
    email_error = request.args.get('email_error')
    return render_template('form.html', username_error=username_error, password_error=password_error, email_error=email_error)

@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    password_v = request.form['password-v']
    email = request.form['email']
    
    #validate username
    username_error = ''
    if len(username) < 3 or len(username) > 20:
        username_error = 'User Names must be between 3 and 20 characters'
    if ' ' in username:
        username_error = 'User Names may not contain spaces'
    if not username:
        username_error = 'Please enter a username'
    
    #validate password
    password_error = ''
    if password != password_v:
        password_error = 'Passwords must match!'
    if len(password) < 3 or len(password) > 20:
        password_error = 'Password must be between 3 and 20 characters'
    if not password:
        password_error = 'Please enter a password'

    #validate email    
    email_error = ''
    if email:
        if len(email) < 3 or len(email) > 20:
            email_error = 'Email must be between 3 and 20 characters'
        if email.count('@') != 1 or email.count('.') != 1:
            email_error = 'Please enter a valid Email address'
        if ' ' in email:
            email_error = 'Please enter a valid Email address'

    if username_error or password_error or email_error:
        return redirect('/?username_error=' + username_error + '&password_error=' + password_error + '&email_error=' + email_error + '&username=' + username + '&email=' + email)
    else:
        return redirect('/welcome?username='+ username)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username )

app.run()