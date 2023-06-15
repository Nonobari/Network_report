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


class PingAddrForm(FlaskForm):
    ip_address = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "IP Address"})
    
    npings = IntegerField(validators=[
        NumberRange(min=1, max=100)], render_kw={"placeholder": "Number of pings"}, default=3)
    
    submit = SubmitField('Ping')

class NmapForm(FlaskForm):
    ip_address = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "IP Address"})
    
    scan_type = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Scan Type"})
  
    ports = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Port(s) to scan"})
    
    submit = SubmitField('Scan')

class DnsReconForm(FlaskForm):
    domain = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Domain name"})
    
    submit = SubmitField('Submit')

class DnsEnumForm(FlaskForm):
    domain = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Domain name"})
    
    submit = SubmitField('Submit')

class TraceRouteForm(FlaskForm):
    domain = StringField(validators=[
        InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Domain name"})
    
    submit = SubmitField('Submit')
