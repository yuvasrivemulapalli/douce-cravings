
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'doucecravingsnew_app'
urlpatterns = [
    path('list/edit/<int:item_id>/', views.edit_view, name='edit_view'),
    path('list/delete/<int:item_id>/', views.delete_view, name='delete_view'),
    path('list', views.list_of_items, name='list_of_items'),
    path('list/<int:item_id>', views.item_details, name='item_details'),
    path('home', views.home, name='home'),
    path('review', views.review, name='review'),
    path('login_page', views.login_page, name='login_page'),
    path('', views.main, name='main'),
    path('list/add/', views.add_view, name='add_view'),
    path('list/add_item/', views.add_item, name='add_item'),
    path('list/sort/', views.sort_items, name='sort-items'),
    path('get_reviews/', views.get_reviews, name='get_reviews'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]
