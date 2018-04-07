from django.conf.urls import url

from . import views
from . import api


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', api.UserRegistrationView.as_view(), name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
