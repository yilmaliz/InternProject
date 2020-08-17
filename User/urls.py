from User import views
from django.urls import path

urlpatterns = [
    path('register', views.CreateUserView.as_view(), name='user'),
    path('user/<int:pk>/settings', views.UserDetail.as_view()),
]
