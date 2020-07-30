from app import app, db
from app.models import Article
from flask import request


# first api call: /add_article
# this call should add a single article and should be accompanied with a dictionary containing
# title and article_body.
@app.route("/add_article", methods=["POST"])
def add_article():
    article = Article(
        title=request.json["title"],
        article_body=request.json["article_body"],
        # date = request.json['date'],
    )
    db.session.add(article)
    db.session.commit()
    return {"message": "success"}
