from config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# the app is represented in our application by the application instance, called 'app'.
app = Flask(__name__)
app.config.from_object(Config)
# the database is going to be represented in the application by the database instance.
db = SQLAlchemy(app)
# The database migration engine also has an instance:
migrate = Migrate(app, db)
