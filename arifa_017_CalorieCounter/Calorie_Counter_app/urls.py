from django.urls import path
from .views import *

urlpatterns = [

    path('', login_page, name = 'login'),
    path('register/', register_page, name = 'register'),
    path('change_password/', change_password, name = 'change_password'),
    path('logout/', logout_page, name = 'logout'),
    path('home/', home, name = 'home'),
    
    path('add_calorie_entry/', add_calorie_entry, name = 'add_calorie_entry'),
    path('view_calorie_entries/', view_calorie_entries, name = 'view_calorie_entries'),
  
    
]