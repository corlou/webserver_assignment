from flask import Flask

from flask_marshmallow import Marshmallow
from database import db

app = Flask(__name__)
ma = Marshmallow(app)


def create_app():

   # Initialise database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:password@localhost:5433/polecalendar2"
    db.init_app(app)

    # Create any tables that don't exist
    with app.app_context():
        db.create_all()

    # Initialise Marshmallow for serialisation
    ma.init_app(app)

    # Register routes
    with app.app_context():
        import routes.root as root_routes
        import routes.dancer as dancer_routes
        import routes.studio as studio_routes
        import routes.event as event_routes
        app.register_blueprint(root_routes.api)
        app.register_blueprint(dancer_routes.api)
        app.register_blueprint(studio_routes.api)
        app.register_blueprint(event_routes.api)
        # app.register_blueprint(registration_routes.api)
        # app.register_blueprint(favourite_routes.api)

    return app


if __name__ == "__main__":
    # Run server
    app = create_app()
    app.run(debug=False)
