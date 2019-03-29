import os
class Configuration(object):
    DEBUG = True

    # __file__ is the full file name (include path) of the module
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))

    # define a sqlalchemy URI
    # dialect+driver://username:password@host:port/database
    # Because SQLite databases are stored in local files, the only information we need to
    # provide is the path to the database file.
    #
    # On the other hand, if you wanted to connect
    # to PostgreSQL running locally, your URI might look something like this:
    # postgresql://postgres:secretpassword@localhost:5432/blog_db

    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
