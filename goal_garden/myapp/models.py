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

class User(models.Model):
    """
    Represents registered users of the system.

    Attributes:
        username (str): The username of the user.
        password (str): The hashed password of the user.
        email (str): The email address of the user.
        phone_number (str): The phone number of the user.
        date_of_birth (DateField): The date of birth of the user.
    """
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, unique=True)
    date_of_birth = models.DateField()

class Profile(models.Model):
    """
    Represents user profiles.

    Attributes:
        user (User): The user associated with the profile.
        bio (str): The biography of the user.
        education (str): The education details of the user.
        job (str): The job details of the user.
        interests (str): The interests of the user.
        privacy_settings (str): The privacy settings of the user.
        profile_picture (BinaryField): The profile picture of the user.
        cover_photo (BinaryField): The cover photo of the user.
        join_date (DateField): The date when the user joined.
        last_active (DateTimeField): The last active date and time of the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    education = models.CharField(max_length=255, blank=True)
    job = models.CharField(max_length=255, blank=True)
    interests = models.CharField(max_length=255, blank=True)
    privacy_settings = models.CharField(max_length=255, choices=PRIVACY)
    profile_picture = models.BinaryField(blank=True)
    cover_photo = models.BinaryField(blank=True)
    join_date = models.DateField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

class Group(models.Model):
    """
    Represents groups created by users.

    Attributes:
        group_name (str): The name of the group.
        description (str): The description of the group.
        member_count (int): The number of members in the group.
        creation_date (DateField): The date when the group was created.
    """
    group_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    member_count = models.BigIntegerField()
    creation_date = models.DateField(auto_now_add=True)

class GroupUser(models.Model):
    """
    Represents the association between users and groups.

    Attributes:
        user (User): The user in the group.
        group (Group): The group the user belongs to.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Message(models.Model):
    """
    Represents messages sent between users.

    Attributes:
        sender (User): The sender of the message.
        receiver (User): The receiver of the message.
        content (str): The content of the message.
        timestamp (DateTimeField): The timestamp when the message was sent.
        status (str): The status of the message.
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=MESSAGE_STATUS)

class Goal(models.Model):
    """
    Represents user goals.

    Attributes:
        user (User): The user associated with the goal.
        profile (Profile): The profile associated with the goal.
        content (str): The content of the goal.
        date_posted (DateField): The date when the goal was posted.
        frequency (str): The frequency of the goal.
        score (int): The score of the goal.
        privacy_settings (str): The privacy settings of the goal.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    date_posted = models.DateField(auto_now_add=True)
    frequency = models.CharField(max_length=255, choices=FREQUENCY)
    score = models.BigIntegerField()
    privacy_settings = models.CharField(max_length=255, choices=PRIVACY)

class Plant(models.Model):
    """
    Represents user's progress on goals.

    Attributes:
        goal (Goal): The goal associated with the plant.
        profile (Profile): The profile associated with the plant.
        streak_alive (bool): Indicates if the streak is alive or not.
        streak_duration (int): The duration of the streak.
        days_streak_dead (int): The number of days the streak is dead.
        days_streak_kept_alive (int): The number of days the streak is kept alive.
    """
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    streak_alive = models.BooleanField(default=True)
    streak_duration = models.BigIntegerField()
    days_streak_dead = models.BigIntegerField()
    days_streak_kept_alive = models.BigIntegerField()

class Comment(models.Model):
    """
    Represents comments made on goals.

    Attributes:
        user (User): The user who made the comment.
        goal (Goal): The goal the comment is associated with.
        content (str): The content of the comment.
        timestamp (DateTimeField): The timestamp when the comment was made.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    """
    Represents likes on goals.

    Attributes:
        goal (Goal): The goal the like is associated with.
        user (User): The user who made the like.
        timestamp (DateTimeField): The timestamp when the like was made.
    """
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Media(models.Model):
    """
    Represents media content associated with goals.

    Attributes:
        goal (Goal): The goal associated with the media.
        user (User): The user who uploaded the media.
        content (BinaryField): The content of the media.
        date_uploaded (DateField): The date when the media was uploaded.
        privacy_settings (str): The privacy settings of the media.
    """
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.BinaryField()
    date_uploaded = models.DateField(auto_now_add=True)
    privacy_settings = models.CharField(max_length=255, choices=PRIVACY)
