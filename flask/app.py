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
        "Implement messaging"
        "About page"
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

"""__flask_wtf_imports__"""
from flask_wtf import FlaskForm

"""__wtforms_imports__"""
from wtforms import (StringField,
                     TextAreaField)

"""__wtforms_validators_imports__"""
from wtforms.validators import DataRequired

"""__datetime_imports__"""
from datetime import datetime

"""__flask_sqlalchemy_imports__"""
from flask_sqlalchemy import (SQLAlchemy)

"""__sqlalchemy_imports__"""
from sqlalchemy import (inspect, 
                        text,
                        Result)

"""__typing_imports__"""
from typing import Any

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

"""__base64_imports__"""
import base64

# Database URI
# Construct the database URI using the database connection parameters
DATABASE_URI = f"mysql://{DATABASES['default']['USER']}:{DATABASES['default']['PASSWORD']}@{DATABASES['default']['HOST']}:{DATABASES['default']['PORT']}/{DATABASES['default']['NAME']}"


# Initialize the Flask application
app = Flask(__name__, static_url_path='/static', template_folder='templates')

# Configure SQLAlchemy database URI and track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set a secret key for the application
app.secret_key = SECRET_KEY

# Configure the logging for the application
dictConfig(LOGGING)

# Import the database models
from db.models import db

# Initialize the database connection
db.init_app(app)

"""__models_imports__[local]"""
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

# Initialize the login manager for user authentication
login_manager = LoginManager()
login_manager.init_app(app)


# ----------------- START SERIALIZE ----------------- #

def serialize(model):
  """
  Serializes a model object into a dictionary.

  Args:
    model: The model object to be serialized.

  Returns:
    A dictionary containing the serialized attributes of the model object.
  """
  return {c.key: getattr(model, c.key)
      for c in inspect(model).mapper.column_attrs}

# ----------------- END SERIALIZE ----------------- #


# ----------------- START ERROR HANDLING ----------------- #

@app.errorhandler(404)
def page_not_found(error):
  """
  Error handler for 404 page not found.
  
  Args:
    error: The error object representing the 404 error.
    
  Returns:
    A rendered template for the 404.html page with a 404 status code.
  """
  return render_template('404.html'), 404


@app.errorhandler(405)
def not_allowed(error):
  """
  Error handler for 405 method not allowed.
  
  Args:
    error: The error object representing the 405 error.
    
  Returns:
    A rendered template for the 405.html page with a 405 status code.
  """
  return render_template('405.html'), 405


@app.errorhandler(500) 
def internal_server_error(error):
  """
  Error handler for internal server errors (HTTP status code 500).
  
  Args:
    error: The error object representing the internal server error.
    
  Returns:
    A rendered template for the '500.html' error page with a 500 status code.
  """
  return render_template('500.html'), 500


@app.errorhandler(403)
def forbidden(error):
  """
  Error handler for 403 Forbidden status code.
  
  This function is called when a 403 Forbidden error occurs in the Flask application.
  It renders the '403.html' template and returns a 403 status code.
  
  Parameters:
    error (Exception): The exception object representing the error.
  
  Returns:
    tuple: A tuple containing the rendered template and the HTTP status code 403.
  """
  return render_template('403.html'), 403


@app.errorhandler(401) 
def internal_server_error(error):
  """
  Error handler for 401 Unauthorized error.
  
  This function is called when a 401 error occurs in the Flask application. It renders the '401.html' template
  and returns a 401 status code.
  
  Parameters:
    error (Exception): The exception object representing the error.
    
  Returns:
    tuple: A tuple containing the rendered template and the HTTP status code 401.
  """
  return render_template('401.html'), 401

# ----------------- END ERROR HANDLING ----------------- #


# ----------------- START BASE ----------------- #

@app.route('/')
def index():
  """
  Renders the base.html template.

  Returns:
    The rendered base.html template.
  """
  return render_template('base.html')
  
  
@app.route('/base')
def base():
  """
  Renders the base.html template.

  Returns:
    The rendered base.html template.
  """
  return render_template('base.html')


@app.route('/about')
def about():
  """
  Renders the about.html template.

  Returns:
    The rendered about.html template.
  """
  return render_template('about.html')

# ----------------- END BASE ----------------- #


# ----------------- START USER ----------------- #

@login_manager.user_loader
def load_user(user_id):
  """
  Load a user from the database based on the user_id.

  Args:
    user_id (int): The ID of the user to load.

  Returns:
    User: The User object corresponding to the user_id.
  """
  return User.query.get(int(user_id))
    
    
@app.route('/login', methods=['GET', 'POST'])
def login():
  """
  Handle the login functionality.

  If the request method is POST, it retrieves the username and password from the form data.
  It then checks if the provided username and password match a user in the database.
  If a match is found, the user is logged in and redirected to their profile page.
  If no match is found, an error message is flashed and the login page is rendered again.

  Returns:
    If the request method is POST and a valid user is found, it redirects to the profile page.
    Otherwise, it renders the login page.
  """
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
  
  
@app.route('/profile')
@login_required
def profile():
  """
  Renders the user profile page with the user's information, goals, and groups.

  Returns:
    A rendered template of the user profile page.
  """
  profile_data = {
    'username': current_user.username,
    'email': current_user.email,
    'profile': Profile.get_profile_by_userid(current_user.userid),
    'goals': Goal.query_goals(),
    'groups': Group.query_groups()
  }
  
  return render_template('user.html', profile_data=profile_data)


@app.route('/user')
def user():
  """
  Renders the user.html template with the user's profile data.

  Returns:
    The rendered user.html template with the profile_data variable.
  """
  profile_data = {
    'username': current_user.username,
    'email': current_user.email,
    'profile': Profile.get_profile_by_userid(current_user.userid),
    'goals': Goal.query_goals(),
    'groups': Group.query_groups()
  }
  return render_template('user.html', profile_data=profile_data)

# ----------------- END USER ----------------- #


# ----------------- START MESSAGING ----------------- #

class MessageForm(FlaskForm):
  """
  Represents a form for sending messages.

  Attributes:
    receiver (StringField): The receiver of the message.
    content (TextAreaField): The content of the message.
  """
  receiver = StringField('Receiver', validators=[DataRequired()])
  content = TextAreaField('Content', validators=[DataRequired()])


@app.route('/message', methods=['GET', 'POST'])
@login_required
def send_message():
  """
  Send a message to another user.

  This function handles the logic for sending a message to another user.
  It validates the form data, checks if the receiver exists, creates a new message,
  and stores it in the database. It also retrieves the received messages for the
  current user and renders the message.html template.

  Returns:
    A rendered template with the message form and received messages.
  """
  form = MessageForm()
  if form.validate_on_submit():
    # Get receiver's ID
    receiver_username = form.receiver.data
    receiver = User.query.filter_by(username=receiver_username).first()
    if not receiver:
      flash('Receiver not found!', 'error')
      return render_template('message.html', form=form)
    
    # Create a new message
    message = Message(useridsender=1, useridreceiver=receiver.userid, content=form.content.data)
    db.session.add(message)
    db.session.commit()
    flash('Message sent successfully!', 'success')
    
  received_messages = Message.query.filter_by(useridreceiver=current_user.userid).all()
  
  return render_template('message.html', form=form, messages=received_messages)

# ----------------- END MESSAGING ----------------- #


# ----------------- START QUERIES ----------------- #
def convert_to_list(results: Result[Any]):
    """
    Convert the result proxy to a list of lists.

    Args:
        results (ResultProxy): The result proxy object to be converted.

    Returns:
        list: A list of lists containing the results.
    """
    labels = results.keys()
    data = results.fetchall()
    list_with_labels = []
    for row in data:
        row_with_labels = {}
        for i, label in enumerate(labels):
            if isinstance(row[i], bytes):
                # Convert binary data to Base64 string
                row_with_labels[label] = base64.b64encode(row[i]).decode('utf-8')
            else:
                row_with_labels[label] = row[i]
        list_with_labels.append(row_with_labels)
    return list_with_labels

@app.route('/query', methods=['GET', 'POST'])
def query():

    query_one = """
        SELECT * FROM 
        (
            SELECT User.UserID, 
                   User.Username,
                   Profile.Bio, 
                   Profile.Education, 
                   Profile.Job
            FROM User
            INNER JOIN Profile ON User.UserID = Profile.UserID 
        ) AS query_one;
    """
    
    query_two = """ 
        SELECT *
        FROM (
            SELECT AVG(StreakDuration) AS average_streak_duration
            FROM Plant
        ) AS query_two;
    """

    query_three = """
        SELECT query_three.GoalsCount, Profile.*
        FROM (
            SELECT COUNT(*) AS GoalsCount, UserID
            FROM Goal
            WHERE UserID IN (
                SELECT UserID
                FROM Profile
                WHERE Job = 'Software Engineer'
            )
            GROUP BY UserID
        ) AS query_three
        INNER JOIN Profile ON query_three.UserID = Profile.UserID;
    """
    
    query_four = """
        SELECT *
        FROM (
            SELECT 
                Goal.UserID,
                COUNT(*) AS TotalGoals,
                AVG(Score) AS AverageScore
            FROM 
                Goal
            WHERE
                PrivacySettings = 'Public'
            GROUP BY 
                Goal.UserID
            HAVING 
                TotalGoals <> 0
                AND AverageScore >= 10
        ) AS query_four;
    """

    query_five = """
        SELECT *
        FROM (
            SELECT User.UserID, User.Username, Goal.Content
            FROM User
            LEFT OUTER JOIN Goal ON User.UserID = Goal.UserID
        ) AS query_five;
    """
    
    results_one = db.session.execute(text(query_one))
    list_one = convert_to_list(results_one)
    
    results_two = db.session.execute(text(query_two))
    list_two = convert_to_list(results_two)
    
    results_three = db.session.execute(text(query_three))
    list_three = convert_to_list(results_three)
    
    results_four = db.session.execute(text(query_four))
    list_four = convert_to_list(results_four)
    
    results_five = db.session.execute(text(query_five))
    list_five = convert_to_list(results_five)
    
    data = {
        "User Profiles": list_one,
        "Average": list_two,
        "Software Engineer": list_three,
        "Users with Public Goals and Average Score >= 10": list_four,
        "Usernames, User IDs, and Associated Goal Content": list_five
    }
    
    return render_template('query_results.html', json_data=data)
    

# ----------------- START QUERIES ----------------- #

@app.route('/ad_hoc', methods=['GET', 'POST'])
def ad_hoc_query():
  """
  Handles ad hoc SQL queries.

  GET method: Renders the ad_hoc_query.html template.
  POST method: Processes the SQL query, checks for prohibited keywords,
  executes the query if safe, and renders the query_results.html template
  with the results or appropriate error message.
  """
  
  json_response_for_insert = {
    "event_raised": "INSERT keyword detected/parsed, the entry was successfully inserted",
    "next_step": "Check relations tab",
    "status": 200
  }
  
  json_response_for_alter = {
    "error": "ALTER detected/parsed, such SQL queries are not allowed without admin status",
    "next_step": "Contact the admin or set permission to \"admin\"",
    "status": 403
  }
  
  json_response_for_drop = {
    "error": "DROP detected/parsed, such SQL queries are not allowed without admin status",
    "next_step": "Contact the admin or set permission to \"admin\"",
    "status": 403
  }
  
  if request.method == 'POST':
    sql_query = request.form.get('sql_query')
    
    # Check SQL_Query for malicious activity
    prohibited_keywords = ['drop', 'alter', 'DROP', 'ALTER']
    json_response_trigger_keyword = ['insert', 'INSERT']
          
    for keyword in prohibited_keywords:
      if keyword.lower() in sql_query.lower():
          if keyword.lower() == 'alter':
              return render_template('query_results.html', json_data=json_response_for_alter)
          elif keyword.lower() == 'drop':
              return render_template('query_results.html', json_data=json_response_for_drop)
    
    # Check for 'insert' keyword
    for keyword in json_response_trigger_keyword:
      if keyword.lower() in sql_query.lower():
        db.session.execute(text(sql_query))
        #return render_template('query_results.html', json_data=json_response_for_insert)
    
    query_result = db.session.execute(text(sql_query))
    list_result = convert_to_list(query_result)
    
    data = {
      "Current Query": list_result,
    }
    return render_template('query_results.html', json_data=data)
  
  else:
    return render_template('ad_hoc_query.html')

# ----------------- START SEARCH ----------------- #

# ----------------- START DB ----------------- #

@app.route('/database', methods=['POST', 'GET'])
def display_db():
  
    table_data = {}

    # Define a dictionary of table names and queries
    queries_dict = {
        "User": "SELECT * FROM `User`;",
        "Profile": "SELECT * FROM `Profile`;",
        "Group": "SELECT * FROM `Group`;",
        "Message": "SELECT * FROM `Message`;",
        "Goal": "SELECT * FROM `Goal`;",
        "Plant": "SELECT * FROM `Plant`;",
        "Comment": "SELECT * FROM `Comment`;",
        "Like": "SELECT * FROM `Like`;",
        "Media": "SELECT * FROM `Media`;",
        "GroupUser": "SELECT * FROM `GroupUser`;"
    }
        
    for table_name, query in queries_dict.items():
      query_result = db.session.execute(text(query))
      table_data[table_name] = convert_to_list(query_result)
      
    return render_template('database.html', data=table_data)
      
# ----------------- START DB ----------------- #

@app.route('/search', methods=['POST'])
def search_users():
  """
  Search for users based on a search query and return the search results.

  Returns:
    If a user is found, returns a rendered template with the search results.
    If no user is found, returns an empty JSON response.
  """
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
    return jsonify([])

# ----------------- END SEARCH ----------------- #

if __name__ == '__main__':
    app.run(debug=True)