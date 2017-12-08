from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms import ValidationError

from flask_wtf.file import FileField, FileRequired, FileAllowed

from .. import texts
from wtforms.validators import Required

import json


class UploadForm(FlaskForm):
	text_file = FileField(validators=[FileAllowed(texts, u'Text Only!'), FileRequired()])
	upload = SubmitField(u'Upload')


class ActionForm(FlaskForm):
	example_stuct = {"key":"item1","pie_data":[1,2,3,4]}
	input_text = TextAreaField(render_kw = {"placeholder":"InputText must be json dict object, which struct like %s" %json.dumps(example_stuct)}, validators=[Required("please input the data")])
	# input_text = TextAreaField(render_kw = {"InputText must be json dict object, which struct like " }, validators=[Required("please input the data")])
	output_text = TextAreaField()
	action = SubmitField(u'Action')
	def validate_input_text(self,field):
		try:
			print("field",field.data)
			field_dict = json.loads(field.data)
			print("field_dict",field_dict)
			if not isinstance(field_dict,dict) or "pie_data" not in field_dict:
				raise ValidationError("InputText must be json dict object, which struct like %s" %json.dumps(example_stuct))
		except Exception as exce:
			print("exec",exec)
			raise ValidationError('InputText must be a json object')



		
