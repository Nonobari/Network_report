# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Create forms to be passed to the frontend
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, Length, ValidationError, NumberRange

class WhoisForm(FlaskForm):
    domain = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "Domain"})
    
    submit = SubmitField('Submit')

class theHarvesterForm(FlaskForm):
    domain = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "Domain"})
    
    limite = IntegerField(validators=[
        NumberRange(min=1, max=3000)], render_kw={"placeholder": "Limit of search results"}, default=1000)
    
    source = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "Source"})
    
    submit = SubmitField('Submit')

class HoleheForm(FlaskForm):
    email = StringField(validators=[
        InputRequired(), Length(min=2, max=300)], render_kw={"placeholder": "E-mail"})
    
    submit = SubmitField('Submit')
