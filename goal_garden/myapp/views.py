from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from django.urls import reverse
from django.template import RequestContext

import os

from .models import (
    User,
    Profile,
    Group,
    Message,
    Goal,
    Plant,
    Comment,
    Like,
    Media,
    Groupuser,
    AuthGroup,
    AuthGroupPermissions,
    AuthPermission,
    AuthUser,
    AuthUserGroups,
    AuthUserUserPermissions,
    DjangoAdminLog,
    DjangoContentType,
    DjangoMigrations,
    DjangoSession,
)



# TODO: fix 403, 404, 500 errors

def yield_file_path(html_file_name: str) -> str:
    """_summary_
    Brief:
        This function returns the path to the html file
    Args:
        html_file_name (str): name of the html file

    Returns:
        str: path to the html file
    """
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', html_file_name)

DATABASE_HTML = yield_file_path("database.html")
INDEX_HTML = yield_file_path("index.html")
HTML_404 = yield_file_path("404.html")
HTML_500 = yield_file_path("500.html")
HTML_403 = yield_file_path("403.html")
USER_HTML = yield_file_path("profile.html")
SEARCH_HTML = yield_file_path("search.html")
GOALS_HTML = yield_file_path("goals.html")
SECURE_HTML = yield_file_path("secure.html")
LOGIN_HTML = yield_file_path("login.html")

def admin_only(view_func):
    """
    Brief:
        This function checks if the user is an admin
    Args:   
        view_func (function): the view function to be checked
        
    Returns:
        function: the wrapper function
    """
    def wrapper_func(request, *args, **kwargs):
        """
        Brief:
            This function checks if the user is an admin   
        Args:
            request (HttpRequest): the request object
            *args: the arguments
            **kwargs: the keyword arguments
            
        Returns:
            function: the view function
        """
        if request.user.is_staff:  
            return view_func(request, *args, **kwargs)
        else:
            return redirect(HTML_403)
    return wrapper_func

def error_403(request, exception):
    """ 
    Brief:
        This function returns the 403 error page
    Args:
        request (HttpRequest): the request object
        exception (Exception): the exception object
            
    Returns:
        HttpResponse: the 403 error page
    """
    return render(request, HTML_403, status=403)

def error_404(request, exception):
    """ 
    Brief:
        This function returns the 404 error page
    Args:
        request (HttpRequest): the request object
        exception (Exception): the exception object
            
    Returns:
        HttpResponse: the 404 error page
    """
    return render(request, HTML_404, status=404)

def error_500(request, exception):
    """ 
    Brief:
        This function returns the 500 error page
    Args:
        request (HttpRequest): the request object
        exception (Exception): the exception object
            
    Returns:
        HttpResponse: the 500 error page
    """
    return render(request, HTML_500, status=500)

@admin_only
def database(request): #to be deleted
    """ 
    Brief:
        This function returns the database page 
    Args:
        request (HttpRequest): the request object
        
    Returns:    
        HttpResponse: the database page
    """
    users = User.objects.all()
    profiles = Profile.objects.all()
    groups = Group.objects.all()
    messages = Message.objects.all()
    goals = Goal.objects.all()
    plants = Plant.objects.all()
    comments = Comment.objects.all()
    likes = Like.objects.all()
    media = Media.objects.all()
    groupusers = Groupuser.objects.all()
    
    authgroups = AuthGroup.objects.all()
    authgrouppermissions = AuthGroupPermissions.objects.all()
    authpermissions = AuthPermission.objects.all()
    authusers = AuthUser.objects.all()
    authusergroups = AuthUserGroups.objects.all()
    authuseruserpermissions = AuthUserUserPermissions.objects.all()
    djangoadminlog = DjangoAdminLog.objects.all()
    djangocontenttype = DjangoContentType.objects.all()
    djangomigrations = DjangoMigrations.objects.all()
    djangosession = DjangoSession.objects.all()
    
    render_dict: dict = {
        'users': users,
        'profiles': profiles,
        'groups': groups,
        'messages': messages,
        'goals': goals,
        'plants': plants,
        'comments': comments,
        'likes': likes,
        'media': media,
        'groupusers': groupusers,
        'authgroups': authgroups,
        'authgrouppermissions': authgrouppermissions,
        'authpermissions': authpermissions,
        'authusers': authusers,
        'authusergroups': authusergroups,
        'authuseruserpermissions': authuseruserpermissions,
        'djangoadminlog': djangoadminlog,
        'djangocontenttype': djangocontenttype,
        'djangomigrations': djangomigrations,
        'djangosession': djangosession,
    }
    
    return render(request, DATABASE_HTML, render_dict)

def index(request):
    """ 
    Brief:
        This function returns the index page
    Args:
        request (HttpRequest): the request object
            
    Returns:
        HttpResponse: the index page
    """
    return render(request, INDEX_HTML)

def search_profiles(request):
    """
    Brief:
        This function returns the search page
    Args:
        request (HttpRequest): the request object
    
    Returns:
        HttpResponse: the search page
        
    Information to display:
        User:
        - Username: VARCHAR(255)
        - Email: VARCHAR(255)
        - DateOfBirth: DATE

        Profile:
        - Bio: VARCHAR(255)
        - Education: VARCHAR(255)
        - Job: VARCHAR(255)
        - Interests: VARCHAR(255)
        - PrivacySettings: ENUM('Public', 'Private', 'Brand', 'Athlete', 'FriendsOnly')
        - ProfilePicture: BLOB
        - CoverPhoto: BLOB
        - JoinDate: DATE
        - LastActive: DATETIME
    """
    search_results = {}
    usernames = User.objects.values_list('username', flat=True) # For autocomplete
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        if search_query:
            # Find users whose username or email matches the search query
            matching_users = User.objects.filter(
                Q(username__icontains=search_query) | Q(email__icontains=search_query)
            )
            if matching_users.exists():
                for user in matching_users:
                    # Access the profile associated with the user
                    try:
                        profile = Profile.objects.get(userid=user.userid)
                        search_results[user.userid] = {
                            'username': user.username,
                            'email': user.email,
                            'dateofbirth': user.dateofbirth,
                            
                            'bio': profile.bio,
                            'education': profile.education,
                            'job': profile.job,
                            'interests': profile.interests,
                            'profile_picture': profile.profilepicture.decode(),
                            'cover_photo': profile.coverphoto.decode(),
                            'join_date': profile.joindate,
                            'last_active': profile.last_active,
                            'privacy_settings': profile.privacysettings
                        }
                    except Profile.DoesNotExist:
                        print("Profile not found for user with id:", user.userid)

            else:
                # No matching users found
                return render(request, HTML_404, status=404)
            
    return render(request, 'search.html', {'search_results': search_results, 'usernames': usernames})

def goals(request):
    """ 
    Brief:
        This function returns the goals page
    Args:
        request (HttpRequest): the request object
            
    Returns:
        HttpResponse: the goals page
    """
    
    return render(request, GOALS_HTML)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Retrieve the hashed password from the database based on the username
        try:
            user = User.objects.get(username=username)
            hashed_password = user.password  # Assuming 'password' field stores the hashed password
            
        except User.DoesNotExist:
            return render(request, LOGIN_HTML, {'error': 'Invalid username or password'})

        if password == hashed_password:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])

            #return redirect('user/') #TODO: redirect to profile
            profile_url = reverse('profile')
            return redirect(profile_url)
        else:
            # Authentication failed, display error message
            return render(request, LOGIN_HTML, context_instance=RequestContext(request))
    else:
        return render(request, LOGIN_HTML)
    
@login_required
def user(request):
    """ 
    Brief:
        This function returns the user page
    Args:
        request (HttpRequest): the request object
            
    Returns:
        HttpResponse: the user page
    """
    #redirects to here after successful login
    logged_in_user = request.user
    return render(request, USER_HTML, {'user': logged_in_user})