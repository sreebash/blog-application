from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),

]
