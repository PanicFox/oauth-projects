import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, redirect, request, session
import requests
from dotenv import load_dotenv
import os

load_dotenv()

#Load Spotify App Credentials
spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
#Other Statics
spotify_redirect_uri='http://127.0.0.1:5000/callback'
app = Flask(__name__)

app.secret_key = "your-secret-key"
sp_oauth = SpotifyOAuth(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri=spotify_redirect_uri,
    #test scopes
    scope="user-library-read playlist-modify-private"
)
@app.route("/")
def index():
    redirect("/login")
@app.route("/login")
def login():
    auth_url = sp_oauth.get_authorize_url()
    session["token_info"] = sp_oauth.get_cached_token()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    token_info = sp_oauth.get_access_token(request.args["code"])
    session["token_info"] = token_info
    print(token_info)

app.run()