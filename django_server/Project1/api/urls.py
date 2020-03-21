from django.contrib import admin
from django.urls import path, re_path, include
from .router import router
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='HelpingHand Project 1 API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/docs', schema_view),
    re_path('api/(?P<version>(v1|v2))/', include(router.urls))
]
