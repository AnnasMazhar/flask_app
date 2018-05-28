from app.catalog import main
from app import db
from app.catalog.models import Novel, Publication
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required
from app.catalog.forms import EditBookForm, CreateBookForm


@main.route('/')
def display_books():

    novels = Novel.query.all()

    return render_template('home.html', novels=novels)


@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):

    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Novel.query.filter_by(pub_id=publisher_id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)


@main.route('/edit/book/<book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Novel.query.get(book_id)
    form = EditBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash('Book Edited Successfully')
        return redirect(url_for('main.display_books'))
    return render_template('edit_book.html', form=form)


@main.route('/create/book/<pub_id>', methods=['GET', 'POST'])
@login_required
def create_book(pub_id):
    form = CreateBookForm()
    form.pub_id.data = pub_id

    if form.validate_on_submit():
        book = Novel(title=form.title.data, author=form.author.data, avg_rating=form.avg_rating.data, image=form.image_url.data, book_format=form.book_format.data, num_pages=form.num_pages.data, pub_id=form.pub_id.data)
        db.session.add(book)
        db.session.commit()
        flash('Book Added Successfully')
        return redirect(url_for('main.display_publisher', publisher_id=pub_id))
    return render_template('create_book.html', form=form, pub_id=pub_id)


@main.route('/book/delete/<book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Novel.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully')
        return redirect(url_for('main.display_books'))
    return render_template('delete_book.html', book=book, book_id=book.id)

