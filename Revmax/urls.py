from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from GreenTaxi import views

urlpatterns = [
    url(r'^GreenTaxi/', include('GreenTaxi.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^status/', views.RequestList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

