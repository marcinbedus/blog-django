from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/add_post/', views.createPost, name="createpost"),
    path('post/<str:pk>/', views.post, name="post"),
    path('post/<str:pk>/add_comment/', views.createComment, name="createcomment"),
]
