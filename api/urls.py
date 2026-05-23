from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogposts/', views.PostListCreate.as_view(), name="blogpost-view-create"),
    path('blogposts/<int:pk>', views.PostRetrieveUpdateDestroy.as_view(), name="blogpost-view-update-delete"),
]
