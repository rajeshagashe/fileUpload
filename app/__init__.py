import os
import importlib

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from app.views import blueprints


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        # load global environments, when not testing
        app.config.from_pyfile("../.env")
        #connect db
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        try:
            # create folder for sqlite
            os.makedirs(app.instance_path)
        except OSError:
            pass
    
    for path, blueprint, url_prefix in blueprints:
        module = importlib.import_module(path)
        app.register_blueprint(getattr(module, blueprint), url_prefix=url_prefix)       
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    CORS(app)
    return app

# migrations -->
# flask db init
# flask db migrate
# flask db upgrade

# from flask_migrate import Migrate 

app = create_app()
# migrate = Migrate(app, **(db conn))