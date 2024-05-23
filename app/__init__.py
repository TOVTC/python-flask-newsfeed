# don't forget to start a virtual environment before installing dependencies so they aren't installed globally
# make sure to run commands in Powershell
# .\venv\Scripts\activate
# your powershell command line should be prefixed with (venv)
# if you get an error, it might be because your execution policy is restricted in Powershell, run as administrator and set the execution policy first

# to run the application use the following command
# python -m flask run

# import Flask function
from flask import Flask
# you can import home directly from the routes package because the __init__.py file imported and renamed the blueprint
# otherwise it would be from app.routes.home import bp as home
# you can also add additional modules to import as a list
from app.routes import home, dashboard
from app.db import init_db
from app.utils import filters

# def keyword to define the create_app() function
# function is defined using whitespace/indents, not curly braces
def create_app(test_config=None):
    # set up app config
    # app should serve static resources from root directory, not default /static directory
    # (trailing slashes are optional - /dashboard == /dashboard/)
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    # add our custom formatting utils to the templates
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural

    # hello is an inner function within the app
    # the @app.route decorator turns this into a route which returns the route's response
    @app.route('/hello')
    def hello():
        return 'hello world'
    
    # register imported routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    # call the init_db() function when the app is ready
    # make sure to pass the app in as an argument so connections can be closed correctly
    init_db(app)
    return app