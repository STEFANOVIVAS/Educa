from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(Profile)
# class UserAdminConfig(UserAdmin):
#     model = User
#     fieldsets = UserAdmin.fieldsets + (
#         ("Personal info", {
#          "fields": ("bio", )}),
#     )
