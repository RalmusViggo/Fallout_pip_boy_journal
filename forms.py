from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
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
    
    submit = SubmitField("> Submit Data")

class RegisterForm(FlaskForm):
    username = StringField("Name", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    origin = StringField("Origin", validators=[InputRequired()])
    origin_trait = StringField("Origin Trait", validators=[InputRequired()])
    strength = IntegerField("Strength", validators=[InputRequired()])
    perception = IntegerField("Perception", validators=[InputRequired()])
    endurance = IntegerField("Endurance", validators=[InputRequired()])
    charisma = IntegerField("Charisma", validators=[InputRequired()])
    intelligence = IntegerField("Intelligence", validators=[InputRequired()])
    agility = IntegerField("Agility", validators=[InputRequired()])
    luck = IntegerField("Luck", validators=[InputRequired()])
    tagskill1 = StringField("Tag Skill 1", validators=[InputRequired()])
    tagskill2 = StringField("Tag Skill 2", validators=[InputRequired()])
    tagskill3 = StringField("Tag Skill 3", validators=[InputRequired()])
    athletics = IntegerField("Athletics", validators=[InputRequired()])
    barter = IntegerField("Barter", validators=[InputRequired()])
    big_guns = IntegerField("Big Guns", validators=[InputRequired()])
    energy_weapons = IntegerField("Energy Weapons", validators=[InputRequired()])
    explosives = IntegerField("Explosives", validators=[InputRequired()])
    lockpick = IntegerField("Lockpick", validators=[InputRequired()])
    medicine = IntegerField("Medicine", validators=[InputRequired()])
    melee_weapons = IntegerField("Melee Weapons", validators=[InputRequired()])
    pilot = IntegerField("Pilot", validators=[InputRequired()])
    repair = IntegerField("Repair", validators=[InputRequired()])
    science = IntegerField("Science", validators=[InputRequired()])
    small_guns = IntegerField("Small Guns", validators=[InputRequired()])
    sneak = IntegerField("Sneak", validators=[InputRequired()])
    speech = IntegerField("Speech", validators=[InputRequired()])
    survival = IntegerField("Survival ",validators= [ InputRequired() ])
    throwing = IntegerField ("Throwing ",validators= [ InputRequired() ])
    unarmed=IntegerField ("Unarmed ",validators= [ InputRequired() ])
    level = IntegerField("Level", validators=[InputRequired()])
    submit = SubmitField("> Submit Data")
    
    

    
""" class LoginForm(FlaskForm):
    name = StringField("Brukernavn", validators=[InputRequired()])
    submit = SubmitField("Logg inn") """