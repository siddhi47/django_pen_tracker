from django.urls import path

from . import views

urlpatterns = [
    path('edit/<str:username>', views.edit_user, name ='edit_user'),
    path('<str:username>', views.user_profile, name ='user_profile'),
    path('signup/',views.sign_up,name = 'signup'),
]
