from flask import Flask

# Note: flask.ext.migrate changed to flask_migrate
#       flask.ext.script changed to flask_migrate
from flask_migrate import Migrate, MigrateCommand

# Note: flask.ext.script changed to flask_script
from flask_script import Manager

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
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


