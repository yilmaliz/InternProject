from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=280)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Tweet.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('title',instance.content)
        instance.date = validated_data.get('title',instance.date)
        instance.save()
        return instance
