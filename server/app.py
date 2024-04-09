from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Create Flask application instance
app = Flask(__name__)

# Configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy object and associate it with the Flask application
db = SQLAlchemy(app)

#using this works when we do flask db init

#db.init_app(app)
#This doesnt 



# Create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# Initialize the Flask application to use the database


if __name__ == '__main__':
    # Run the Flask application on port 5555 with debugging enabled
    app.run(port=5555, debug=True)
