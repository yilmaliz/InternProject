from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name


class Tweet(models.Model):
    content = models.CharField(max_length=280)
    begeniSayisi = models.IntegerField(default=0)
    yorumSayisi = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)






