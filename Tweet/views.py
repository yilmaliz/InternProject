from .models import Tweet
from .serializers import TweetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class TweetViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # def list(self, request):
    #     tweets = Tweet.objects.all()
    #     serializer = TweetSerializer(tweets, many=True)
    #     return Response(serializer.data)
    #
    # def create(self, request):
    #     serializer = TweetSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Tweet.objects.all()
    #     tweet = get_object_or_404(queryset, pk=pk)
    #     serializer = TweetSerializer(tweet)
    #     return Response(serializer.data)
    #
    # def update(self, request, pk=None):
    #     tweet = Tweet.objects.get(pk=pk)
    #     serializer = TweetSerializer(tweet, data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






#
# class GenericAPIViewDetail(generics.GenericAPIView, mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     serializer_class = TweetSerializer
#     queryset = Tweet.objects.all()
#
#     lookup_field = 'id'
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, id =None):
#         return self.retrieve(request)
#
#     def put(self,request, id=None):
#         return self.update(request,id)
#
#     def delete(self,request,id):
#         return self.destroy(request,id)
#
#
#
# class GenericAPIViewList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     serializer_class = TweetSerializer
#     queryset = Tweet.objects.all()
#     lookup_field = 'id'
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, id =None):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
#
# class TweetAPIView(APIView):
#
#     def get(self, request):
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TweetSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class TweetDetails(APIView):
#
#     def get_object(self,id):
#         try:
#             return Tweet.objects.get(id=id)
#
#         except Tweet.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, id):
#         tweet = self.get_object(id)
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         tweet = self.get_object(id)
#         serializer = TweetSerializer(tweet, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def __delete__(self, request, id):
#         tweet = self.get_object(id)
#         tweet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET','POST'])
# def tweet_list(request):
#
#     if request.method == 'GET':
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TweetSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def tweet_detail(request, pk):
#     try:
#         tweet = Tweet.objects.get(pk=pk)
#     except Tweet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#
#
#        serializer = TweetSerializer(tweet, data=request.data)
#
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         tweet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)