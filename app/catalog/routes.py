from app.catalog import main
from app import db
from app.catalog.models import Novel, Publication
from flask import render_template


@main.route('/')
def display_books():

    novels = Novel.query.all()

    return render_template('home.html', novels=novels)


@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):

    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Novel.query.filter_by(pub_id=publisher_id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)
