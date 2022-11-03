import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'pythoncoder112@gmail.com'
    MAIL_PASSWORD = 'daxlrxbwlwremntf'


# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USERNAME'] = 'pythoncoder112@gmail.com'
# app.config['MAIL_PASSWORD'] = 'daxlrxbwlwremntf'

# 'pythoncoder112@gmail.com'
# 'daxlrxbwlwremntf'

# SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
