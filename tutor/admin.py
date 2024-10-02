from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from tutor.models import Error, User

@admin.register(User)
class UserAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    pass

@admin.register(Error)
class ErrorAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    pass


