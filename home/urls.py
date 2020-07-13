from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.user_info, name='user-info' ),
    path('team/',views.user_team,name = "user-team"),
    path('about/',views.user_about,name = "user-about"),
    path('contact/',views.user_contact,name = "user-contact"),
    
]