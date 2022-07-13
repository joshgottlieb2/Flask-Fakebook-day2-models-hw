from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    migrate = Migrate()

    db.init_app(app)
    migrate.init_app(app, db)


    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.blueprints.blog import bp as blog_bp
    app.register_blueprint(blog_bp)


    return app