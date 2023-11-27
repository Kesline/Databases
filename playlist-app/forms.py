# forms.py
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    
    name = StringField('Playlist Name', validators=[DataRequired()])

class SongForm(FlaskForm):
    """Form for adding songs."""
    
    title = StringField('Song Title', validators=[DataRequired()])

class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to a playlist."""
    
    song = SelectField('Song To Add', coerce=int, validators=[DataRequired()])
