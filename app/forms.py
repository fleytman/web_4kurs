from flask.ext.wtf import Form
from wtforms import IntegerField
from wtforms.validators import Required


class SearchForm(Form):
    search = IntegerField('GTIN', validators = [Required()])
