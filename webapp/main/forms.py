from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed

from .. import texts
# from wtforms.validators import Required



class UploadForm(FlaskForm):
	input_text = TextAreaField(render_kw = {"placeholder": "current only support txt file"})
	text_file = FileField(validators=[FileAllowed(texts, u'Text Only!'), FileRequired(u'Choose a file!')])
	submit = SubmitField(u'Upload')
		
