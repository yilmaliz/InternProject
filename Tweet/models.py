from django.db import models


class Tweet(models.Model):
    content = models.CharField(max_length=280)
    begeniSayisi = models.IntegerField(default=0)
    yorumSayisi = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)






