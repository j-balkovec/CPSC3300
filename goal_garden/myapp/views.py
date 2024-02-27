from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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
HTML_403 = yield_file_path("admin.html")

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
def database(request):
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