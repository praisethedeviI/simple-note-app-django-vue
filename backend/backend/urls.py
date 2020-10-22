from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


urlpatterns = [
    url(r'^api/v1/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
]
