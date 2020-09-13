from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User', related_name='tweets', on_delete=models.CASCADE,null=True)
    class Meta:
        ordering = ('date',)
    def save(self, *args, **kwargs):
        super(Tweet, self).save(*args, **kwargs)
    def __str__(self):
        return self.content


class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='commentTweet',on_delete=models.CASCADE,null=True)

    #parent = models.IntegerField(null=True,verbose_name='Tweet ID')

    comment = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    owner = models.ForeignKey(
        'auth.User', related_name='comments', on_delete=models.CASCADE,null=True)
    class Meta:
        ordering = ('date',)
    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
    def __str__(self):
        return self.content

class Like(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='likeTweet',on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    owner = models.ForeignKey(
        'auth.User', related_name='likes', on_delete=models.CASCADE, null=True)
    class Meta:
        #unique_together = ['tweet', 'owner']
        ordering = ('date',)
    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)
    def __str__(self):
        return self.id