from flaskblog import app
from flaskblog import db
from flask import os


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    if not os.path.exists('site.db'):
        db.create_all()
    app.run(debug=True)