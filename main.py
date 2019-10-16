from flask import Flask, render_template, request, redirect
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True



def username_error(username):
    space = False
    for char in username:
        if char.isspace() == True:
            space = True
    

    if 2 < len(username) < 20 and space == False :
        return False
    else:
        return True

def password_error(password):
    space = False
    for char in password:
        if char.isspace() == True:
            space = True
    
    if 2<len(password)<20 and space == False:
        return False
    else:
        return True

def verify_error(verify, password):
    if verify == password:
        return False
    else:
        return True

def email_error(email):
    if "@" in email and "." in email and " " not in email and 2<len(email)<20 and email.count('@') == 1:
        return False
    else:
        return True


@app.route("/")
def index():
    return render_template('base.html', username='', username_error='', password='', password_error='', verify='', verify_password_error='', email='', email_error='')

@app.route("/signup", methods=['POST'])
def validate():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    un_error = ''
    pw_error = ''
    v_error = ''
    e_error = ''

    # 'escape' the user's input so that if they typed HTML, it doesn'
    username_escaped = cgi.escape(username, quote=True)
    password_escaped = cgi.escape(password, quote=True)
    verify_escaped = cgi.escape(verify, quote=True)
    email_escaped = cgi.escape(email, quote=True)

         
    if username_error(username):
        un_error = "Please specify a username that is between 3 and 20 characters and contains no spaces."
        username = ''

    if password_error(password):
        pw_error = "Please specify a password that is between 3 and 20 characters and contains no spaces."
        password = ''

    if verify_error(verify, password):
        v_error = "Passwords do not match."

    if email_error(email):
        e_error = "Please specify a valid email."
        email = ''

    if not username_error(username) and not password_error(password) and not verify_error(verify, password) and not email_error(email):
        return render_template('welcome.html', username=username)
    else:
        return render_template('base.html', username=username, username_error=un_error, password_error=pw_error, verify_password_error=v_error, email=email, email_error=e_error)
        

       

app.run()




