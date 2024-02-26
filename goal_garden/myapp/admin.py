from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(Goal)
admin.site.register(Plant)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Media)
admin.site.register(Groupuser)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)
