from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, FloatField
from wtforms.validators import DataRequired


class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    num_pages = StringField('Pages', validators=[DataRequired()])
    submit = SubmitField('Update')


class CreateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    avg_rating = FloatField('Rating', validators=[DataRequired()])
    image_url = StringField('Img_URL', validators=[DataRequired()])
    book_format = StringField('Format', validators=[DataRequired()])  # type: StringField
    num_pages = IntegerField('NumofPages', validators=[DataRequired()])
    pub_id = IntegerField('Pub_id', validators=[DataRequired()])
    submit = SubmitField('Create')

