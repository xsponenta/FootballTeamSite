"Forms file"

from PIL import Image, UnidentifiedImageError
from flask_wtf import FlaskForm, file
from wtforms import StringField, SubmitField, TextAreaField, \
    DateTimeLocalField, IntegerField, \
    SelectMultipleField, widgets, RadioField, SelectField, FileField
from wtforms.validators import InputRequired, ValidationError

class MultiCheckboxField(SelectMultipleField):
    "Multi check box field"
    widget = widgets.ListWidget(prefix_label=True)
    option_widget = widgets.CheckboxInput()

    def __init__(self, label=None, validators=None, default=None, **kwargs):
        super(MultiCheckboxField, self).__init__(label, validators, **kwargs)
        self.default = default

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist
        else:
            self.data = self.default

class PlayerForm(FlaskForm):
    "PLayer form"
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    nickname = StringField("Nickname", validators=[InputRequired()])
    position = SelectField("Gender", choices=[("Goalkeeper", "Goalkeeper"),
                ("Defender", "Defender"), ("Midfielder", "Midfielder"),
                ("Attacker", "Attacker")], validators=[InputRequired()])
    picture = FileField("Photo", validators=[InputRequired(), file.FileAllowed(['jpg', 'png', 'jpeg'])])

    submit = SubmitField("Add")

    def validate_picture(self, picture) -> None:
        "Validates picture"
        if picture.data.filename != '':
            try:
                Image.open(picture.data)
            except UnidentifiedImageError as exc:
                raise ValidationError("Imported file seems to be corrupted") from exc

class UpdatePlayerForm(FlaskForm):
    "PLayer form"
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])
    nickname = StringField("Nickname", validators=[InputRequired()])
    position = SelectField("Gender", choices=[("Goalkeeper", "Goalkeeper"),
                ("Defender", "Defender"), ("Midfielder", "Midfielder"),
                ("Attacker", "Attacker")], validators=[InputRequired()])
    picture = FileField("Photo", validators=[file.FileAllowed(['jpg', 'png', 'jpeg'])])

    submit = SubmitField("Update")

    def validate_picture(self, picture) -> None:
        "Validates picture"
        if picture.data.filename != '':
            try:
                Image.open(picture.data)
            except UnidentifiedImageError as exc:
                raise ValidationError("Imported file seems to be corrupted") from exc

class MatchForm(FlaskForm):
    "Match Form"
    start_time = DateTimeLocalField('Start time', validators=[InputRequired()],
            format='%Y-%m-%dT%H:%M')
    rival_team = StringField('Rival Team', validators=[InputRequired()])
    team_score = IntegerField('Team Score', validators=[InputRequired()])
    rival_score = IntegerField('Rival Score', validators=[InputRequired()])
    players = MultiCheckboxField("Players", choices=[])
    
    submit = SubmitField("Add")
    
class StatisticForm(FlaskForm):
    "Statistic Form"
    hits_team = IntegerField('Hits Team', validators=[InputRequired()])
    hits_rival = IntegerField('Hits Rival', validators=[InputRequired()])
    hits_gate_team = IntegerField('Hits Gate Team', validators=[InputRequired()])
    hits_gate_rival = IntegerField('Hits Gate Rival', validators=[InputRequired()])
    falls_team = IntegerField('Falls Team', validators=[InputRequired()])
    falls_rivals = IntegerField('Falls Rivals', validators=[InputRequired()])
    yellow_cards_team = IntegerField('Yellow cards Team', validators=[InputRequired()])
    yellow_cards_rival = IntegerField('Yellow cards Rival', validators=[InputRequired()])
    red_cards_team = IntegerField('Red cards Team', validators=[InputRequired()])
    red_cards_rival = IntegerField('Red cards Rival', validators=[InputRequired()])
    offsides_team = IntegerField('Offsides Team', validators=[InputRequired()])
    offsides_rivals = IntegerField('Offsides Rival', validators=[InputRequired()])
    corners_team = IntegerField('Corners Team', validators=[InputRequired()])
    corners_rivals = IntegerField('Corners Rival', validators=[InputRequired()])

    submit = SubmitField("Edit")

class HighlightForm(FlaskForm):
    "Highlight Form"
    title = StringField("Title", validators=[InputRequired(), file.FileAllowed(['mp4', 'mov'])])
    video = FileField("Video")

    submit = SubmitField("Add")
# class TrailForm(FlaskForm):
#     "Trail form"
#     name = StringField("Name", validators=[InputRequired()])
#     length = IntegerField("Length", validators=[InputRequired()])
#     elevation_gain = IntegerField("Elevation gain", validators=[InputRequired()])
#     description = TextAreaField("Description (optional)")

#     submit = SubmitField("Insert")

# class HikeForm(FlaskForm):
#     "Hike form"
#     start_time = DateTimeLocalField('Start time', validators=[InputRequired()],
#             format='%Y-%m-%dT%H:%M')
#     end_time = DateTimeLocalField('End time', validators=[InputRequired()],
#             format='%Y-%m-%dT%H:%M')
#     trails = RadioField('Select trail', choices=[], validators=[InputRequired()])

#     submit = SubmitField("Insert")

# class HikerForm(FlaskForm):
#     "Hiker form"
#     first_name = StringField("First Name", validators=[InputRequired()])
#     last_name = StringField("Last Name", validators=[InputRequired()])
#     age = IntegerField("Age", validators=[InputRequired()])
#     gender = SelectField("Gender", choices=[("Male", "Male"), ("Female", "Female")], validators=[InputRequired()])
#     experience_level = SelectField("Experience Level", choices=[("Noob", "Noob"), 
#         ("Intermediate", "Intermediate"), ("Expert", "Expert")], validators=[InputRequired()])
#     hikes = RadioField('Select hike', choices=[], validators=[InputRequired()])
    
#     submit = SubmitField("Insert")
    