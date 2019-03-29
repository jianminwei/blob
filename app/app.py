from flask import Flask
# flask extention has SQLAlchemy extention for Flask using SQLAlchemy.

# Note: flask.ext.sqlalchemy is changed to flask_sqlalchemy
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


from config import Configuration # import our configuration data.

app = Flask(__name__)
app.config.from_object(Configuration) # use values from our Configuration object

# this will instruct our Flask app, and in turn SQLAlchemy, how to
# communicate with our application's database.
db = SQLAlchemy(app)
