from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('users_edit', views.users_edit, name='users_edit'),
    path('user_details/<str:username>/', views.user_details, name='user_details'),
]
