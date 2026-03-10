from django.contrib import admin
from .models import AuthUserModel, CalorieEntryModel

admin.site.register([AuthUserModel, CalorieEntryModel])


