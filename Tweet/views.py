from django.contrib.auth.models import User


from .models import Tweet, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import TweetSerializer, UserSerializer, CommentSerializer
from rest_framework import  viewsets, permissions


# class TweetList(APIView):
#
#     def get(self,request, format=None):
#         tweets =Tweet.objects.all()
#         serializer = TweetSerializer(tweets,many=True)
#
#         return Response(serializer.data)

#
#
#     def post(self,request,format=None):
#         serializer = TweetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#
# class TweetDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Tweet.objects.get(pk=pk)
#         except Tweet.DoesNotExist:
#             raise Http404
#     def get(self,request,pk,format=None):
#         tweet = self.get_object(pk)
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data)
#     def put(self,request,pk,format=None):
#         tweet = self.get_object(pk)
#         serializer = TweetSerializer(tweet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['GET','POST'])
# def tweet_list(request):
#     if request.method == 'GET':
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = TweetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','PUT','DELETE'])
# def tweet_detail(request, pk):
#     try:
#         tweet = Tweet.objects.get(pk=pk)
#     except Tweet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#        serializer = TweetSerializer(tweet, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         tweet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class MixinTweetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# class MixinTweetDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
# class TweetMixin(object):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#     def pre_save(self,obj):
#         obj.owner =self.request.user
#
#
# class GenericTweetList(generics.ListCreateAPIView):
#
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
# class GenericTweetDetail(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer

class TweetViewSet(viewsets.ModelViewSet):

    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer



