from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

API_TITLE = 'Pastebin API'
API_DESCRIPTION = 'A Web API for creating and viewing highlighted code snippets.'
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tweet.urls')),
    path('', include('User.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]