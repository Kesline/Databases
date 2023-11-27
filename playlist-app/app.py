from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    songs = db.relationship('Song', secondary='playlist_song', back_populates='playlists')


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    playlists = db.relationship('Playlist', secondary='playlist_song', back_populates='songs')


class PlaylistSong(db.Model):
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)


class PlaylistForm(FlaskForm):
    name = StringField('Playlist Name', validators=[DataRequired()])


class SongForm(FlaskForm):
    title = StringField('Song Title', validators=[DataRequired()])


class NewSongForPlaylistForm(FlaskForm):
    song = SelectField('Song To Add', coerce=int, validators=[DataRequired()])


@app.route("/")
def root():
    return redirect(url_for('show_all_playlists'))


@app.route("/playlists")
def show_all_playlists():
    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()
    form.song.choices = [(song.id, song.title) for song in Song.query.all()]
    return render_template("playlist_detail.html", playlist=playlist, form=form)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    form = PlaylistForm()
    if form.validate_on_submit():
        playlist = Playlist(name=form.name.data)
        db.session.add(playlist)
        db.session.commit()
        return redirect("/playlists")
    return render_template("add_playlist.html", form=form)


@app.route("/songs")
def show_all_songs():
    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    song = Song.query.get_or_404(song_id)
    return render_template("song_detail.html", song=song)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    form = SongForm()
    if form.validate_on_submit():
        song = Song(title=form.title.data)
        db.session.add(song)
        db.session.commit()
        return redirect("/songs")
    return render_template("add_song.html", form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()
    form.song.choices = [(song.id, song.title) for song in Song.query.filter(~Song.playlists.contains(playlist)).all()]

    if form.validate_on_submit():
        playlist_song = PlaylistSong(song_id=form.song.data, playlist_id=playlist_id)
        db.session.add(playlist_song)
        db.session.commit()
        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
