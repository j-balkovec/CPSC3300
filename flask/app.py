"""__doc__
__auth__: Jakob Balkovec
__version__: 1.0
__date__: 2024-03-03
__status__: In Development
__file__: app.py

__desc__: Main file for the Flask application. This file will be used to run
          the application and handle all the routes and views.

__bugs__: None

todo_list = {
    "TODAY": [
        "Add a new user",
        "Fix username potentially (not a big deal)",
        "Implement search",
        "Implement messaging"
    ],
    "CURRENT": [
        'Implementing search"
    ].
    "TOMORROW": [],
    "URGENT": [],
    "NOT IMPORTANT": [
        "Implementing to show only the Groups a current user is a part of"
    ]
}
"""

"""__flask_imports__"""
from flask import (Flask, 
                   render_template, 
                   request, 
                   redirect, 
                   url_for,
                   flash,
                   jsonify,
                   session)

"""__logging_imports__"""
from logging.config import dictConfig

"""__flask_sqlalchemy_imports__"""
from flask_sqlalchemy import SQLAlchemy

"""__flask_login_imports__"""
from flask_login import (LoginManager, 
                         UserMixin, 
                         login_user, 
                         current_user,
                         login_required)

"""__secrets_imports__[local]"""
from db.secrets import (DATABASES,
                        PASSWORD,
                        SECRET_KEY,
                        LOGGING)

# Database URI
# Construct the database URI using the database connection parameters
DATABASE_URI = f"mysql://{DATABASES['default']['USER']}:{DATABASES['default']['PASSWORD']}@{DATABASES['default']['HOST']}:{DATABASES['default']['PORT']}/{DATABASES['default']['NAME']}"


app = Flask(__name__, static_url_path='/static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = SECRET_KEY

#config logging
dictConfig(LOGGING)

from db.models import db

db.init_app(app)

from db.models import (User,
                       Profile,
                       Group,
                       Message,
                       Goal,
                       Plant,
                       Comment,
                       Like,
                       Media,
                       GroupUser,)


login_manager = LoginManager()
login_manager.init_app(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500) 
def internal_server_error(error):
    return render_template('500.html'), 500

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.route('/')
def index():
    return render_template('base.html')
  
@app.route('/base')
def base():
    return render_template('base.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.get_by_username_and_password(username, password)
        if user:
            login_user(user, force=True)
            flash('Logged in successfully.', 'success')
            next_page = request.args.get('next')
            return redirect(url_for('profile'))  # Redirect to the user page
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html')
  
# Profile page
@app.route('/profile')
@login_required
def profile():
  
    profile_data = {
        'username': current_user.username,
        'email': current_user.email,
        'profile': Profile.get_profile_by_userid(current_user.userid),
        'goals': Goal.query_goals(),
        'groups': Group.query_groups()
    }
    
    return render_template('user.html', profile_data=profile_data)

# renders upon search
@app.route('/user')
def user():
    # User works
    profile_data = {
        'username': current_user.username,
        'email': current_user.email,
        'profile': Profile.get_profile_by_userid(current_user.userid),
        'goals': Goal.query_goals(),
        'groups': Group.query_groups()
    }
    return render_template('user.html', profile_data=profile_data)

@app.route('/search', methods=['POST'])
def search_users():
    search_query = request.json.get('search_query', '')
    user = User.query.filter(User.username.like(f'%{search_query}%')).first()
    if user:
        profile = Profile.get_profile_by_userid(user.userid)
        search_results = {
            'username': user.username,
            'email': user.email,
            'profile': profile,
            'goals': Goal.query_goals(),
            'groups': Group.query_groups()
        }
        return render_template('search_user.html', profile_data=search_results)
    else:
      return jsonify([])  # Or return an appropriate message
   
if __name__ == '__main__':
    app.run(debug=True)