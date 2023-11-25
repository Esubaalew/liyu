from django.urls import path
from . import views
from django.views.generic import RedirectView
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', RedirectView.as_view(url='posts/'), name='post'),
    path('/<str:param1>/<int:param2>/', views.post_detail, name='post_detail'),


]