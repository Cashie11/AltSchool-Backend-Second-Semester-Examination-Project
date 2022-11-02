import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'pythoncoder112@gmail.com'
app.config['MAIL_PASSWORD'] = 'daxlrxbwlwremntf'
mail = Mail(app)

from flaskblog import routes

# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


# The libraries i use for my project are...

# *Html
# *css
# *Bootstrap
# *Python
# *Flask Framework

# about the project, it's a Tech Blog website which a User can create account,login,logout,update his / her details or info,change profile picture and finally the user can make a post too.
# And it's a website by which knowledge are being share, both topics,subjects and information are being share and to help new tech aspirant to acquire more knowledge 
# and it can help a newbie in there difficulties too so they can solve there issues only by one search..those who are already good can jhelp in sharing there knowledge too....check it out
# it's a nice website i promise and changes will be occuring at any time too