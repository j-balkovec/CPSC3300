from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

#django.contrib.auth.hashers.make_password(password, salt=None, hasher='default')

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
USER_HTML = yield_file_path("user.html")
SEARCH_HTML = yield_file_path("search.html")
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
    
    return render(request, '''GOALS_HTML''')
    
def login_view(request):
    next_url = request.GET.get('next', '')  # Get the 'next' parameter from the query string

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:  # Redirect to the 'next' URL if it exists
                return redirect(next_url)
            else:
                return redirect('user')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password', 'next': next_url})
    else:
        return render(request, 'login.html', {'next': next_url})  # Pass 'next' to the login page for redirect purposes

def login_view5(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
            return redirect('login')

        try:
            db_user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
        
        db_password = db_user.password

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', '')  # Get the next URL from the POST data
            if next_url:
                return redirect(next_url)
            else:
                return redirect('user')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, LOGIN_HTML, {'error': messages.get_messages(request), 'next': request.GET.get('next', '')})


# Change login when you get to creating new users
def login_view4(request):
    error = "\0" # Empty str to avoid error
    hashed_password = "\0" # Empty str to avoid error
    next_url = request.GET.get('next', '')  # Get the next URL from the query parameters

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST.get('next', '')
        
        try:
            user = User.objects.get(username=username)
            password = user.password 
            user = authenticate(request, username=username, password=hashed_password)
            print("DEBUG: ", user)
        except User.DoesNotExist:
            return render(request, LOGIN_HTML, {'error': 'User does not exist', 'next': next_url})

        if user is not None:
            login(request, user) 
            if next_url:
                return redirect(next_url)  # Redirect to the next URL
            else:
                return redirect('user')  # Redirect to profile page
            
        else:
            # Authentication failed, display error message
            error = 'Invalid username or password'
            return render(request, LOGIN_HTML, {'error': error, 'next': next_url})
    else:
        return render(request, LOGIN_HTML, {'error': error, 'next': next_url})

def login_view2(request):
    error = ""  # Empty str to avoid error
    next_url = request.GET.get('next', '')  # Get the next URL from the query parameters

    if request.method == 'POST':
        print(request.POST)
        
        username = request.POST['username']
        entered_password = request.POST['password']
        next_url = request.POST.get('next', '')
        
        try:
            user = User.objects.get(username=username)
            if check_password(entered_password, user.password):
                user = authenticate(request, username=username, password=entered_password)
                print("DEBUG: AUTH successfull")
                
            if not check_password(entered_password, user.password):
                raise User.DoesNotExist
        except User.DoesNotExist:
            return render(request, LOGIN_HTML, {'error': 'Invalid username or password', 'next': next_url})

        login(request, user) 
        if next_url:
            return redirect(next_url)  # Redirect to the next URL
        else:
            return redirect('user')  # Redirect to profile page
    else:
        return render(request, LOGIN_HTML, {'error': error, 'next': next_url})

def login_view3(request):
    user = None
    debug_data = {}
    error = ""  # Empty str to avoid error
    next_url = request.GET.get('next', '')  # Get the next URL from the query parameters

    if request.method == 'POST':
        username = request.POST['username']
        entered_password = request.POST['password']
        next_url = request.POST.get('next', '')

        try:
            user = User.objects.get(username=username)
            debug_data['database_password'] = user.password  # Include database password in debug data
            if check_password(entered_password, user.password):
                user = authenticate(request, username=username, password=entered_password)
                debug_data['authentication_status'] = 'success'
                if user is not None:
                    login(request, user) 
                    if next_url:
                        return redirect(next_url)  # Redirect to the next URL
                    else:
                        return redirect('user')  # Redirect to profile page
                else:
                    error = 'User authentication failed'
            else:
                error = 'Invalid username or password'
        except User.DoesNotExist:
            error = 'Invalid username or password'

        debug_data = {
            'user': user,
            'username': username,
            'entered_password': entered_password,
            'next_url': next_url
        }
                
        debug_data['error'] = error  # Include error message in debug data
        print("DEBUG DATA:", debug_data)

    return render(request, LOGIN_HTML, {'error': error, 'next': next_url})

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
    print("DEBUG: logged_in_user:", logged_in_user)
    print(f"DEBUG: user is None: {logged_in_user is None}")
    return render(request, USER_HTML, {'user': logged_in_user})