from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.urls import path
#from .views import tweet_list, tweet_detail
from Tweet import views


router = DefaultRouter()
router.register(r'tweet', views.TweetViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'like', views.LikeViewSet)

urlpatterns = [
    # path('tweet/', tweet_list),
    # path('tweet/<int:pk>/',tweet_detail),
    #
    # path('api/tweet',views.TweetList.as_view()),
    # path('api/tweet/<int:pk>',views.TweetDetail.as_view()),
    #
    # path('mixin/tweet',views.MixinTweetList.as_view()),
    # path('mixin/tweet/<int:pk>',views.MixinTweetDetail.as_view()),
    #
    # path('generic/tweet',views.GenericTweetList.as_view()),
    # path('generic/tweet/<int:pk>',views.GenericTweetDetail.as_view()),

    url(r'^', include(router.urls)),


]