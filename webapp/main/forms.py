from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed

from .. import texts
from wtforms.validators import Required



class UploadForm(FlaskForm):
	text_file = FileField(validators=[FileAllowed(texts, u'Text Only!'), FileRequired()])
	upload = SubmitField(u'Upload')


class ActionForm(FlaskForm):
	input_text = TextAreaField(render_kw = {"placeholder": "Input data or Upload txt data file"}, validators=[Required("please input the data")])
	output_text = TextAreaField()
	action = SubmitField(u'Action')
		
