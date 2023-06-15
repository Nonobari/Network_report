# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Create forms to be passed to the frontend
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, Length, ValidationError

class hydraForm(FlaskForm):
    loginPath = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "loginPath"})
    
    passPath = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "passPath"})
    
    host = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "host"})
    
    service = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "service"})
    
    submit = SubmitField('Submit')

class sqlmapForm(FlaskForm):
    
    url = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "url"})
    
    submit = SubmitField('Submit')