from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5  # This should now work with Bootstrap-Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.choices import SelectField
from wtforms.fields.datetime import TimeField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, URL, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField('Add Book')

all_books = []

@app.route('/')
def home():
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book = {
            "title": form.book_name.data,
            "author" : form.book_author.data,
            "rating" : form.rating.data
        }
        all_books.append(new_book)
        print(new_book)
        print(all_books)
    return render_template('add.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)