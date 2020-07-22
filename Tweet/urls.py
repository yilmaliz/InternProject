
from django.urls import path,include
from .views import  TweetViewSet
#tweet_list,tweet_detail,TweetAPIView,TweetDetails,GenericAPIViewDetail,GenericAPIViewList,
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tweet', TweetViewSet, basename='tweet')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),


    # #path('tweet/', tweet_list),
    # path('tweet/', TweetAPIView.as_view()),
    # #path('detail/<int:pk>/',tweet_detail)
    # path('detail/<int:id>/',TweetDetails.as_view()),
    # path('generic/tweet/', GenericAPIViewList.as_view()),
    # path('generic/tweet/<int:id>/', GenericAPIViewDetail.as_view()),
]
