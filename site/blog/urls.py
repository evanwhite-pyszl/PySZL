from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.overview, name='overview'),
    path('<int:post_id>/', views.post_view, name='post'),
]