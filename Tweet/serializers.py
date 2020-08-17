from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tweet, Comment


class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    number_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ['url','id','content','owner','date','number_of_comments']

    def get_number_of_comments(self,obj):
        return Comment.objects.filter(tweet=obj.id).count()

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = "__all__"

class SerializerComments(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model =Comment
        fields = ['owner','comment']
class UserSerializer(serializers.HyperlinkedModelSerializer):
    tweets = serializers.HyperlinkedRelatedField(
        many=True, view_name='tweet-detail', read_only=True)

    comments = SerializerComments(many=True)


    class Meta:
        model = User
        fields = ('url','id','username','email','tweets','comments')

