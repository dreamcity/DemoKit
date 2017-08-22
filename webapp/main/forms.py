from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed

from .. import photos
# from wtforms.validators import Required


class UploadForm(FlaskForm):
	photo = FileField(validators=[FileAllowed(photos, u'Image Only!'), FileRequired(u'Choose a file!')])
	submit = SubmitField(u'Upload')
