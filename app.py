import json
import requests

from oauthlib.oauth2 import WebApplicationClient
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from core.Database import db
from core.User import User
from core.Admin import Admin
from core.System import System

GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.secret_key = "fdfhs34h23jbmbfg23b4jhfg"

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app, add_context_processor=True)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

SystemController = System()
UserController = User()

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@login_manager.unauthorized_handler
def unauthorized():
    return "You must be logged in to access this content.", 403

@login_manager.user_loader
def load_user(user_id):
    return UserController.getUserById(user_id)

@app.route("/")
def index():
    return render_template("main.html", user=current_user)

@app.route("/edit_profile", methods = ['POST', 'GET'])
@login_required
def edit_profile():
    if request.method == 'POST':
        name = request.form['name']
        about = request.form['description']
        UserController.editUserProfile(current_user.id, name, about)
        return redirect(url_for("view_profile", user_id="my"))
    
    return render_template("edit-user.html", user=current_user)

@app.route("/view_profile/<user_id>", methods = ['POST', 'GET'])
@login_required
def view_profile(user_id):
    if user_id == "my" or None:
        user_id = current_user.id
    profile = UserController.getUserById(user_id)
    if not profile:
        return "Profile not found!", 404
    return render_template("user-profile.html", user=current_user)

@app.route("/login")
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def login_callback():
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
        if not SystemController.isEmailAllowedToLogin(users_email):
            return "Your email not allowed, contact with administrator", 400
    else:
        return "User email not available or not verified by Google.", 400

    if not UserController.getUserById(user_id=unique_id):
        UserController.createUser(unique_id, users_name, users_email, picture)
    user = UserController.getUserById(unique_id)
        
    login_user(user)
    return redirect(url_for("index"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/temp_admin", methods = ['POST', 'GET'])
def temp_admin():
    if request.method == 'POST':
        email = request.form['email']
        Admin().allowUserEmail(email)
    return render_template("temp_admin.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    context = ('certificate/cert.pem', 'certificate/private.key')
    app.run(host='0.0.0.0', port='5000', ssl_context=context, debug=False)
