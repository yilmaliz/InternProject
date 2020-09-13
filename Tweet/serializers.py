from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tweet, Comment, Like
from rest_framework.validators import UniqueTogetherValidator

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ['id','owner','comment','url','tweet']
class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['url','owner','tweet']

class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    number_of_comments = serializers.SerializerMethodField()
    number_of_likes = serializers.SerializerMethodField()
    commentTweet = CommentSerializer(many=True,read_only=True)
    likeTweet = LikeSerializer(many=True,read_only=True)

    class Meta:
        model = Tweet
        fields = ['url','id','content','owner','date','number_of_comments','commentTweet','likeTweet','number_of_likes']

    def get_number_of_comments(self,obj):
        return Comment.objects.filter(tweet=obj.id).count()
    def get_number_of_likes(self,obj):
        return Like.objects.filter(tweet=obj.id).count()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tweets = serializers.HyperlinkedRelatedField(
        many=True, view_name='tweet-detail', read_only=True)

    comments = CommentSerializer(many=True)

    class Meta:
        model = User
        fields = ('url','id','username','email','tweets','comments')

