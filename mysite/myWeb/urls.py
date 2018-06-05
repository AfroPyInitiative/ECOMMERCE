from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.hello),
    url(r'^date/$', views.current_date),
    url(r'^date/(\d{1,2})/$', views.hours_ahead),
]