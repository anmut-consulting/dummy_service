import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # The flask-sqlalchemy extension takes the location of the application's database from the SQLALCHEMY_DATABASE_URI
    # configuration variable. It is in general good practice to set configuration from environment variables, and provide
    # a fallback value when the environment does not define the variable.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    # SQLALCHEMY_TRACK_MODIFICATIONS configuration option is set to False to disable a feature of flask-sqlalchemy which
    # signals the application every time a change is about to be made to the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
