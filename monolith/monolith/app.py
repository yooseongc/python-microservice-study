import os
from flask import Flask
from monolith.database import db, User
from monolith.views import blueprints
from monolith.auth import login_manager


def create_app():
    app = Flask(__name__)
    app.config["WTF_CSRF_SECRET_KEY"] = "A SECRET KEY"
    app.config["SECRET_KEY"] = "ANOTHER ONE"
    app.config["STRAVA_CLIENT_ID"] = os.environ["STRAVA_CLIENT_ID"]
    app.config["STRAVA_CLIENT_SECRET"] = os.environ["STRAVA_CLIENT_SECRET"]
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///temp/runnerly"
    
    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app
        
    db.init_app(app)
    login_manager.init_app(app)
    db.create_all(app=app)
    
    with app.app_context():
        q = db.session.query(User).filter(User.email == "tarek@ziade.org")
        user = q.first()
        if user is None:
            tarek = User()
            tarek.email = "tarek@ziade.org"
            tarek.is_admin = True
            tarek.set_password("ok")
            db.session.add(tarek)
            db.session.commit()
            
    return app
