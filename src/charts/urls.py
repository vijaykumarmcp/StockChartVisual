
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/data/$',views.ChartData.as_view(),name='chart-data-view'),
]