from flask import Flask
from flask_sqlalchemy import SQLAlchemy #object relational management(orm)

app=Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

from routes import *

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__=='__main__':
    app.run(debug=True)