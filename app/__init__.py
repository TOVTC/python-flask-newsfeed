# import Flask function
from flask import Flask
# you can import home directly from the routes package because the __init__.py file imported and renamed the blueprint
# otherwise it would be from app.routes.home import bp as home
# you can also add additional modules to import as a list
from app.routes import home, dashboard

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

    # hello is an inner function within the app
    # the @app.route decorator turns this into a route which returns the route's response
    @app.route('/hello')
    def hello():
        return 'hello world'
    
    # register imported routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    return app