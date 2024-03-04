"""
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

from flask import (Flask, 
                   render_template, 
                   request, 
                   redirect, 
                   url_for,
                   flash,
                   jsonify,
                   session)

import logging
from logging.config import dictConfig

from flask_sqlalchemy import SQLAlchemy

from flask_login import (LoginManager, 
                         UserMixin, 
                         login_user, 
                         current_user,
                         login_required)

from db.secrets import (DATABASES,
                        PASSWORD,
                        SECRET_KEY,
                        LOGGING)

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
    # Add groups

from flask import redirect, url_for

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
        print("search_results: ", search_results)
        return render_template('search_user.html', profile_data=search_results)
        #return redirect(url_for('user.html', profile_data=search_results))
    else:
      print("\n\n\nHERE\n\n\n")
      return jsonify([])  # Or return an appropriate message

@app.route('/user_with_profile')
def user_with_profile():
  return render_template('user.html')
   



if __name__ == '__main__':
    app.run(debug=True)