"""Initialize Flask blueprints."""
"""step 1: Import the required libraries"""
from .auth import auth_routes

"""step 2: Define the register_blueprints function"""
def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(auth_routes)
    


    
    