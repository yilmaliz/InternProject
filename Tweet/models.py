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
    tweet = models.IntegerField(null=True)
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
