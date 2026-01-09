from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    gender = StringField("Gender", validators=[InputRequired()])
    age = StringField("Age", validators=[InputRequired()])
    blood_type = StringField("Blood Type", validators=[InputRequired()])
    known_diseases = StringField("Known Diseases", validators=[InputRequired()])
    family = StringField("Family", validators=[InputRequired()])
    current_medical_conditions = StringField("Current Medical Conditions", validators=[InputRequired()])
    previous_medical_conditions = StringField("Previous Medical Conditions", validators=[InputRequired()])
    allergies = StringField("Allergies", validators=[InputRequired()])
    strengths = StringField("Strengths", validators=[InputRequired()])
    
    submit = SubmitField("Submit Data")

""" class LoginForm(FlaskForm):
    name = StringField("Brukernavn", validators=[InputRequired()])
    submit = SubmitField("Logg inn") """