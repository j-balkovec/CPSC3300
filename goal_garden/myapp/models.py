"""
Author: Jakob Balkovec
Date of Creation: Sun 25th Feb 2023
Date of Last Modification: Sun 25th Feb 2023

File: models.py
Description: This file contains the database models for the Q_Project Milestone 1 application.
"""

"""__imports__"""
from django.db import models

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

from django.db import models

class User(models.Model):
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

    userid = models.IntegerField(db_column='UserID', primary_key=True)   
    username = models.CharField(db_column='Username', unique=True, max_length=255, blank=True, null=True)   
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)   
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)   
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)   
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)   

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the User model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'User'

class Profile(models.Model):
    """
    Represents a user profile.

    Attributes:
        profileid (int): The ID of the profile (primary key).
        userid (User): The user associated with the profile.
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

    profileid = models.IntegerField(db_column='ProfileID', primary_key=True)   
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')   
    bio = models.CharField(db_column='Bio', max_length=255, blank=True, null=True)   
    education = models.CharField(db_column='Education', max_length=255, blank=True, null=True)   
    job = models.CharField(db_column='Job', max_length=255, blank=True, null=True)   
    interests = models.CharField(db_column='Interests', max_length=255, blank=True, null=True)   
    privacysettings = models.CharField(db_column='PrivacySettings', max_length=11, blank=True, null=True)   
    profilepicture = models.TextField(db_column='ProfilePicture', blank=True, null=True)   
    coverphoto = models.TextField(db_column='CoverPhoto', blank=True, null=True)   
    joindate = models.DateField(db_column='JoinDate', blank=True, null=True)   
    lastactive = models.DateTimeField(db_column='LastActive', blank=True, null=True)   

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__

    class Meta:
        """
        Meta class for the Profile model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'Profile'
            
class Group(models.Model):
    """
    Represents a group in the application.

    Attributes:
        groupid (int): The ID of the group (primary key).
        groupname (str): The name of the group.
        description (str): The description of the group.
        membercount (int): The number of members in the group.
        creationdate (date): The date when the group was created.
    """
    groupid = models.IntegerField(db_column='GroupID', primary_key=True)   
    groupname = models.CharField(db_column='GroupName', max_length=255, blank=True, null=True)   
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)   
    membercount = models.BigIntegerField(db_column='MemberCount', blank=True, null=True)   
    creationdate = models.DateField(db_column='CreationDate', blank=True, null=True)   
    
    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the Group model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'Group'

class Groupuser(models.Model):
    """
    Model representing the relationship between a user and a group.
    
    Attributes:
        groupuserid (int): The ID of the group user.
        userid (ForeignKey): The user associated with the group user.
        groupid (ForeignKey): The group associated with the group user.
    """
    groupuserid = models.IntegerField(db_column='GroupUserID', primary_key=True)   
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')   
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='GroupID')   

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the GroupUser model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'GroupUser'

class Message(models.Model):
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
    messageid = models.IntegerField(db_column='MessageID', primary_key=True)   
    useridsender = models.ForeignKey('User', models.DO_NOTHING, db_column='UserIDSender')   
    useridreceiver = models.ForeignKey('User', models.DO_NOTHING, db_column='UserIDReceiver')   
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)   
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)   
    status = models.CharField(db_column='Status', max_length=9, blank=True, null=True)   

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the Message model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'Message'

class Goal(models.Model):
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

    goalid = models.IntegerField(db_column='GoalID', primary_key=True)  
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  
    profileid = models.ForeignKey('Profile', models.DO_NOTHING, db_column='ProfileID')  
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  
    dateposted = models.DateField(db_column='DatePosted', blank=True, null=True)   
    frequency = models.CharField(db_column='Frequency', max_length=7, blank=True, null=True)   
    score = models.BigIntegerField(db_column='Score', blank=True, null=True)   
    privacysettings = models.CharField(db_column='PrivacySettings', max_length=11, blank=True, null=True)   

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the Goal model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'Goal'

class Plant(models.Model):
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
        managed (bool): Indicates whether the model's database table is managed by Django.
        db_table (str): The name of the database table associated with the model.
    """
    plantid = models.IntegerField(db_column='PlantID', primary_key=True)   
    goalid = models.ForeignKey(Goal, models.DO_NOTHING, db_column='GoalID')   
    profileid = models.ForeignKey('Profile', models.DO_NOTHING, db_column='ProfileID')   
    streakalive = models.IntegerField(db_column='StreakAlive', blank=True, null=True)   
    streakduration = models.BigIntegerField(db_column='StreakDuration', blank=True, null=True)   
    daysstreakdead = models.BigIntegerField(db_column='DaysStreakDead', blank=True, null=True)   
    daysstreakkeptalive = models.BigIntegerField(db_column='DaysStreakKeptAlive', blank=True, null=True)   

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the Plant model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'Plant'
 
class Comment(models.Model):
    """
    Represents a comment made by a user on a goal.

    Attributes:
        commentid (int): The unique identifier for the comment.
        userid (ForeignKey): The foreign key to the User model representing the user who made the comment.
        goalid (ForeignKey): The foreign key to the Goal model representing the goal on which the comment was made.
        content (str): The content of the comment.
        timestamp (datetime): The timestamp when the comment was made.
    """
    commentid = models.IntegerField(db_column='CommentID', primary_key=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')
    goalid = models.ForeignKey('Goal', models.DO_NOTHING, db_column='GoalID')
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the Comment model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'Comment'
                     
class Like(models.Model):
    """
    Model representing a like on a goal by a user.
    
    Attributes:
        likeid (int): The unique identifier for the like.
        goalid (Goal): The goal that was liked.
        userid (User): The user who liked the goal.
        timestamp (datetime): The timestamp when the like was created.
    """
    likeid = models.IntegerField(db_column='LikeID', primary_key=True)   
    goalid = models.ForeignKey(Goal, models.DO_NOTHING, db_column='GoalID')   
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')   
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)   

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the Like model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'Like'

class Media(models.Model):
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
    mediaid = models.IntegerField(db_column='MediaID', primary_key=True)   
    goalid = models.ForeignKey(Goal, models.DO_NOTHING, db_column='GoalID')   
    content = models.TextField(db_column='Content', blank=True, null=True)   
    dateuploaded = models.DateField(db_column='DateUploaded', blank=True, null=True)   
    privacysettings = models.CharField(db_column='PrivacySettings', max_length=11, blank=True, null=True)   
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')   

    def __str__(self) -> str:
        """
        Returns a string representation of the media object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the Media model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'Media'   

'''__note__
    * The classes/subclasses below are generated by Django and are not part of the original model.
    * They are included here for reference only.
'''
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)
    
    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the AuthGroup model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        The Meta class provides additional options for the model.

        Attributes:
            managed (bool): Indicates whether the table is managed by Django's database migrations.
            db_table (str): The name of the database table for the model.
            unique_together (tuple): A tuple of field names that should be unique together.
        """
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        The Meta class provides additional options for the model.

        Attributes:
            managed (bool): Indicates whether the table is managed by Django's database migrations.
            db_table (str): The name of the database table for the model.
            unique_together (tuple): A tuple of field names that should be unique together.
        """
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the AuthUser model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__

    class Meta:
        """
        The Meta class provides additional options for the model.

        Attributes:
            managed (bool): Indicates whether the table is managed by Django's database migrations.
            db_table (str): The name of the database table for the model.
            unique_together (tuple): A tuple of field names that should be unique together.
        """
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__

    class Meta:
        """
        The Meta class provides additional options for the model.

        Attributes:
            managed (bool): Indicates whether the table is managed by Django's database migrations.
            db_table (str): The name of the database table for the model.
            unique_together (tuple): A tuple of field names that should be unique together.
        """
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__

    class Meta:
        """
        Meta class for the DjangoAdminLog model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__

    class Meta:
        """
        The Meta class provides additional options for the model.

        Attributes:
            managed (bool): Indicates whether the table is managed by Django's database migrations.
            db_table (str): The name of the database table for the model.
            unique_together (tuple): A tuple of field names that should be unique together.
        """
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the DjangoMigrations model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    def __str__(self) -> str:
        """
        Returns a string representation of the user object, which is just the class name.
        
        Returns:
            str: The class name.
        """
        return self.__class__.__name__
    
    class Meta:
        """
        Meta class for the DjangoSession model.
        
        Attributes:
            managed (bool): Indicates whether the model's database table is managed by Django.
            db_table (str): The name of the database table associated with the model.
        """
        managed = False
        db_table = 'django_session'
