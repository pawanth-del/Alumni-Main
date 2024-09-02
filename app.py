from flask import Flask, render_template
from models import db, User  # Import db and User from models.py
from flask_migrate import Migrate

app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nitrkl_alumni.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    # Query the database for attendees with 'completed' status
    attendees = User.query.filter_by(order_status='completed').all()
    
    # Render the index.html template and pass the attendees list to it
    return render_template('index.html', attendees=attendees)


# New registration route
@app.route('/registration')
def registration():
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)
