"""
_author_: Jakob Balkovec
_date_: Sun 25th Feb 2023
_date_of_last_mod_: Sun 25th Feb 2023

_file_: db/models.py
_desc_: This file contains the database models for the Q_Project Milestone 1 application.
"""

"""
_bugs_: {bug1: "The User model does not have a relationship with the Profile model."}
        {bug2: define the tables with __tablename__ and redife realtionships by referencing tablenaem}
"""

"""_imports_"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import relationship

"""
Defines choices for message status.

MESSAGE_STATUS:
- 'sent': Indicates that the message has been sent.
- 'delivered': Indicates that the message has been delivered to the recipient.
- 'read': Indicates that the message has been read by the recipient.
"""
MESSAGE_STATUS = (
  ('sent', 'Sent'),
  ('delivered', 'Delivered'),
  ('read', 'Read'),
)

"""
Defines choices for privacy settings.

PRIVACY:
- 'public': Indicates that the content is visible to the public.
- 'private': Indicates that the content is visible only to the user.
- 'brand': Indicates that the content is associated with a brand.
- 'athlete': Indicates that the content is associated with an athlete.
- 'friendsonly': Indicates that the content is visible only to friends.
"""
PRIVACY =  (
  ('public', 'Public'),
  ('private', 'Private'),
  ('brand', 'Brand'),
  ('athlete', 'Athlete'),
  ('friendsonly', 'FriendsOnly'),
)

"""
Defines choices for goal frequency.

FREQUENCY:
- 'daily': Indicates a goal that occurs daily.
- 'weekly': Indicates a goal that occurs weekly.
- 'monthly': Indicates a goal that occurs monthly.
- 'yearly': Indicates a goal that occurs yearly.
"""
FREQUENCY = (
  ('daily', 'Daily'),
  ('weekly', 'Weekly'),
  ('monthly', 'Monthly'),
  ('yearly', 'Yearly'),
)

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    """
    Represents a user in the system.

    Attributes:
        userid (int): The unique identifier for the user.
        username (str): The username of the user.
        password (str): The password of the user.
        email (str): The email address of the user.
        phonenumber (str): The phone number of the user.
        dateofbirth (date): The date of birth of the user.
    """
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phonenumber = db.Column(db.String(255))
    dateofbirth = db.Column(db.Date)
    
    profiles = db.relationship('Profile', backref='user', lazy=True, uselist=False)
    #messages_sent = db.relationship('Message', foreign_keys='Message.useridsender', backref='sender', lazy=True)
    #messages_received = db.relationship('Message', foreign_keys='Message.useridreceiver', backref='receiver', lazy=True)
    goals = db.relationship('Goal', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    likes = db.relationship('Like', backref='user', lazy=True)
    media = db.relationship('Media', backref='user', lazy=True)
    
    @classmethod
    def get_by_username_and_password(cls, username, password):
        return cls.query.filter_by(username=username, password=password).first()
    
    @property
    def is_authenticated(self):
        # Check if the user has provided valid credentials
        # For simplicity, assume all users are authenticated
        return True

    @property
    def is_active(self):
        # Check if the user's account is active
        return False

    @property
    def is_anonymous(self):
        # Assume all authenticated users are not anonymous
        return False

    def get_id(self):
        # Return the string representation of the user's ID
        return str(self.userid)

    def __repr__(self):
        """
        Returns a string representation of the user object.
        
        Returns:
            str: The string representation.
        """
        return f"User('{self.username}', '{self.email}')"

class Profile(db.Model):
    """
    Represents a user profile.

    Attributes:
        profileid (int): The ID of the profile (primary key).
        userid (int): The user associated with the profile.
        bio (str): The biography of the user.
        education (str): The education information of the user.
        job (str): The job information of the user.
        interests (str): The interests of the user.
        privacysettings (str): The privacy settings of the user.
        profilepicture (str): The URL of the profile picture.
        coverphoto (str): The URL of the cover photo.
        joindate (date): The date when the user joined.
        lastactive (datetime): The last active timestamp of the user.
    """

    __tablename__ = 'profile'
    
    profileid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('User.userid'), nullable=False)
    bio = db.Column(db.String(255))
    education = db.Column(db.String(255))
    job = db.Column(db.String(255))
    interests = db.Column(db.String(255))
    privacysettings = db.Column(db.String(11))
    profilepicture = db.Column(db.String)
    coverphoto = db.Column(db.String)
    joindate = db.Column(db.Date)
    lastactive = db.Column(db.DateTime)

    user_profile = db.relationship("User", backref="profile")
    #groups = db.relationship('GroupUser', backref='profile', lazy=True)
    #goals = db.relationship('Goal', backref='profile', lazy=True)
    #plants = db.relationship('Plant', backref='profile', lazy=True)

    @classmethod
    def get_profile_by_userid(cls, userid):
        profile = cls.query.filter_by(userid=userid).first()
        if profile:
            return {
                'bio': profile.bio,
                'education': profile.education,
                'job': profile.job,
                'interests': profile.interests,
                'profile_picture': profile.profilepicture.decode('utf-8'),
                'cover_photo': profile.coverphoto.decode('utf-8'),
                'join_date': profile.joindate,
                'last_active': profile.lastactive,
            }
        else:
            return None
          
    def __repr__(self):
        """
        Returns a string representation of the profile object.
        
        Returns:
            str: The string representation.
        """
        return f"Profile(profileid={self.profileid}, userid={self.userid})"
      
class Group(db.Model):
    """
    Represents a group in the application.

    Attributes:
        groupid (int): The ID of the group (primary key).
        groupname (str): The name of the group.
        description (str): The description of the group.
        membercount (int): The number of members in the group.
        creationdate (date): The date when the group was created.
    """
    groupid = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(255))
    description = db.Column(db.String(255))
    membercount = db.Column(db.BigInteger)
    creationdate = db.Column(db.Date)

    User = db.relationship('GroupUser', backref='group', lazy=True)
    #members = db.relationship("Profile", secondary="group_user", backref="groups")
     
    def __repr__(self):
        """
        Returns a string representation of the group object.
        
        Returns:
            str: The string representation.
        """
        return f"Group(groupid={self.groupid}, groupname={self.groupname})"
    
    @classmethod
    def query_groups(cls):
        """
        Query all groups from the database and return their information as a list of dictionaries.

        Returns:
            list: A list of dictionaries containing group information.
        """
        groups = Group.query.all()
        group_data = []
        for group in groups:
            group_dict = {
                'groupname': group.groupname,
                'description': group.description,
                'membercount': group.membercount
            }
            group_data.append(group_dict)
        return group_data
      
class GroupUser(db.Model):
    """
    Model representing the relationship between a user and a group.
    
    Attributes:
        groupuserid (int): The ID of the group user.
        userid (ForeignKey): The user associated with the group user.
        groupid (ForeignKey): The group associated with the group user.
    """
    groupuserid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('User.userid', ondelete='CASCADE'))
    groupid = db.Column(db.Integer, db.ForeignKey('group.groupid', ondelete='CASCADE'))

    def __repr__(self):
        """
        Returns a string representation of the GroupUser object.
        
        Returns:
            str: The string representation.
        """
        return f"GroupUser(groupuserid={self.groupuserid}, userid={self.userid}, groupid={self.groupid})"

class Message(db.Model):
    """
    Model representing a message.

    Attributes:
        messageid (int): The ID of the message (primary key).
        useridsender (ForeignKey): The ID of the user who sent the message.
        useridreceiver (ForeignKey): The ID of the user who received the message.
        content (str): The content of the message.
        timestamp (datetime): The timestamp when the message was sent.
        status (str): The status of the message.
    """
    messageid = db.Column(db.Integer, primary_key=True)
    useridsender = db.Column(db.Integer, db.ForeignKey('User.userid', ondelete='CASCADE'))
    useridreceiver = db.Column(db.Integer, db.ForeignKey('User.userid', ondelete='CASCADE'))
    content = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(9), nullable=True)

    def __repr__(self):
        """
        Returns a string representation of the Message object.
        
        Returns:
            str: The string representation.
        """
        return f"Message(messageid={self.messageid}, useridsender={self.useridsender}, useridreceiver={self.useridreceiver}, content={self.content}, timestamp={self.timestamp}, status={self.status})"

class Goal(db.Model):
    """
    Represents a goal in the application.

    Attributes:
        goalid (int): The ID of the goal (primary key).
        userid (ForeignKey): The ID of the user associated with the goal.
        profileid (ForeignKey): The ID of the profile associated with the goal.
        content (str): The content of the goal.
        dateposted (date): The date when the goal was posted.
        frequency (str): The frequency of the goal.
        score (int): The score of the goal.
        privacysettings (str): The privacy settings of the goal.
    """

    goalid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('User.userid', ondelete='CASCADE'))
    profileid = db.Column(db.Integer, db.ForeignKey('profile.profileid', ondelete='CASCADE'))
    content = db.Column(db.String(255), nullable=True)
    dateposted = db.Column(db.Date, nullable=True)
    frequency = db.Column(db.String(7), nullable=True)
    score = db.Column(db.BigInteger, nullable=True)
    privacysettings = db.Column(db.String(11), nullable=True)

    user_goal = db.relationship('User', backref='goal', lazy=True)
    #plants = db.relationship('Plant', backref='goal', lazy=True)
    #comments = db.relationship('Comment', backref='goal', lazy=True)
    #likes = db.relationship('Like', backref='goal', lazy=True)
    #media = db.relationship('Media', backref='goal', lazy=True)
    
    def __repr__(self):
        """
        Returns a string representation of the Goal object.
        
        Returns:
            str: The string representation.
        """
        return f"Goal(goalid={self.goalid}, userid={self.userid}, profileid={self.profileid}, content={self.content}, dateposted={self.dateposted}, frequency={self.frequency}, score={self.score}, privacysettings={self.privacysettings})"
    
    @classmethod
    def query_goals(cls):
        """
        Query all goals from the database and return their information as a list of dictionaries.

        Returns:
            list: A list of dictionaries containing goal information.
        """
        goals = Goal.query.all()
        goal_data = []
        for goal in goals:
            goal_dict = {
                'content': goal.content,
                'frequency': goal.frequency,
                'score': goal.score
            }
            goal_data.append(goal_dict)
        return goal_data
      
class Plant(db.Model):
    """
    Represents a plant in the goal garden.

    Attributes:
        plantid (int): The ID of the plant (primary key).
        goalid (Goal): The goal associated with the plant.
        profileid (Profile): The profile associated with the plant.
        streakalive (int): The number of days the streak is alive.
        streakduration (int): The duration of the streak.
        daysstreakdead (int): The number of days the streak is dead.
        daysstreakkeptalive (int): The number of days the streak is kept alive.

    Meta:
        managed (bool): Indicates whether the model's database table is managed by Flask-SQLAlchemy.
        db_table (str): The name of the database table associated with the model.
    """
    plantid = db.Column(db.Integer, primary_key=True)
    goalid = db.Column(db.Integer, db.ForeignKey('goal.goalid', ondelete='CASCADE'))
    profileid = db.Column(db.Integer, db.ForeignKey('profile.profileid', ondelete='CASCADE'))
    streakalive = db.Column(db.Integer, nullable=True)
    streakduration = db.Column(db.BigInteger, nullable=True)
    daysstreakdead = db.Column(db.BigInteger, nullable=True)
    daysstreakkeptalive = db.Column(db.BigInteger, nullable=True)

    def __repr__(self):
        """
        Returns a string representation of the Plant object.
        
        Returns:
            str: The string representation.
        """
        return f"Plant(plantid={self.plantid}, goalid={self.goalid}, profileid={self.profileid}, streakalive={self.streakalive}, streakduration={self.streakduration}, daysstreakdead={self.daysstreakdead}, daysstreakkeptalive={self.daysstreakkeptalive})"

class Comment(db.Model):
    """
    Represents a comment made by a user on a goal.

    Attributes:
        commentid (int): The unique identifier for the comment.
        userid (ForeignKey): The foreign key to the User model representing the user who made the comment.
        goalid (ForeignKey): The foreign key to the Goal model representing the goal on which the comment was made.
        content (str): The content of the comment.
        timestamp (datetime): The timestamp when the comment was made.
    """
    commentid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('User.userid', ondelete='CASCADE'))
    goalid = db.Column(db.Integer, db.ForeignKey('goal.goalid', ondelete='CASCADE'))
    content = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        """
        Returns a string representation of the Comment object.
        
        Returns:
            str: The string representation.
        """
        return f"Comment(commentid={self.commentid}, userid={self.userid}, goalid={self.goalid}, content={self.content}, timestamp={self.timestamp})"

class Like(db.Model):
    """
    Model representing a like on a goal by a user.
    
    Attributes:
        likeid (int): The unique identifier for the like.
        goalid (Goal): The goal that was liked.
        userid (User): The user who liked the goal.
        timestamp (datetime): The timestamp when the like was created.
    """
    likeid = db.Column(db.Integer, primary_key=True)
    goalid = db.Column(db.Integer, db.ForeignKey('goal.goalid', ondelete='CASCADE'))
    userid = db.Column(db.Integer, db.ForeignKey('User.userid', ondelete='CASCADE'))
    timestamp = db.Column(db.DateTime, nullable=True)
    
    user_like = db.relationship('User', backref='like', lazy=True)
    def __repr__(self):
        """
        Returns a string representation of the Like object.
        
        Returns:
            str: The string representation.
        """
        return f"Like(likeid={self.likeid}, goalid={self.goalid}, userid={self.userid}, timestamp={self.timestamp})"

class Media(db.Model):
    """
    Model representing media files associated with a goal in the application.
    
    Attributes:
        mediaid (int): The unique identifier for the media file.
        goalid (Goal): The foreign key to the associated goal.
        content (str): The content of the media file.
        dateuploaded (date): The date when the media file was uploaded.
        privacysettings (str): The privacy settings for the media file.
        userid (User): The foreign key to the user who uploaded the media file.
    """
    mediaid = db.Column(db.Integer, primary_key=True)
    goalid = db.Column(db.Integer, db.ForeignKey('goal.goalid', ondelete='CASCADE'))
    content = db.Column(db.Text, nullable=True)
    dateuploaded = db.Column(db.Date, nullable=True)
    privacysettings = db.Column(db.String(11), nullable=True)
    userid = db.Column(db.Integer, db.ForeignKey('User.userid', ondelete='CASCADE'))

    def __repr__(self):
        """
        Returns a string representation of the Media object.
        
        Returns:
            str: The string representation.
        """
        return f"Media(mediaid={self.mediaid}, goalid={self.goalid}, content={self.content}, dateuploaded={self.dateuploaded}, privacysettings={self.privacysettings}, userid={self.userid})"
