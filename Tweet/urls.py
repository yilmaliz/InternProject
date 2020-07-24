
from django.urls import path
from .views import tweet_list,tweet_detail

urlpatterns = [
    path('tweet/', tweet_list),
    path('detail/<int:pk>/',tweet_detail)

]
