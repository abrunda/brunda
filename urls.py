from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.today_is),
    url(r'^admin/', admin.site.urls),
]
