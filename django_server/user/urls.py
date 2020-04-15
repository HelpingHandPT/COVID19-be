from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'api/users^$', views.MyUserCreate.as_view(), name='user-create'),
]