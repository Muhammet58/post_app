from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('post/detail/<int:id>/<slug:slug>', views.post_details, name="post_details"),
    path('create_post', views.create_post_view, name='create_post_url'),
    path('delete/<int:post_id>', views.post_delete, name="delete"),
    path('post_edit/<slug:post_slug>', views.edit_post, name='edit_post'),
]
