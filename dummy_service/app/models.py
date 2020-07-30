from app import db


# the data that will be stored in the database will be represented by a collection of classes,
# usually called database models. The ORM layer within SQLAlchemy will do the translations required
# to map objects created from these classes into rows in the proper database tables.
# The user class inherits from db.Model, a base class for all models from Flask-SQLalchemy.
# This class defines several fields as class variables. Fields are created as instances of the db.Column
# class, which takes the field type as an argument, plus other optional arguments that, for example,
# allow me to indicate which fields are unique and indexed, which is important so that database
# searches are efficient.
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    article_body = db.Column(db.String(120), index=True)
    # date = db.Column(db.DateTime, index=True, unique=False)
    # we add here a relationship field. this is not an actual database field, but a high level view of the
    # relationship between users and posts. For a one-to-many relationship, a db.relationship field is normally
    # defined on the "one" side, and is used as a convenient way to get access to the 'many'. The first argument
    # to db.relationship is the model class that represents the "many" side of the relationship, "Post" in this case,
    # added as a string with the class name if the model is defined later in the module. The backref argument defines
    # the name of a field that will be added to the objects of the "many" class that points back at the "one" object.
    # This will add a post.author expression that will return the user given a post. The lazy argument defines how the
    # database query for the relationship will be issued.
    # posts = db.relationship("Post", backref="author", lazy="dynamic")

    # The __repr__ method tells Python how to print objects of this class, which is going to be
    # useful for debugging.
    def __repr__(self):
        return "<Article {}>".format(self.title)
