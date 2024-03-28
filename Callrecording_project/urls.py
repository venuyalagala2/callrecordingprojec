"""
URL configuration for Callrecording_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recordapp.views import CreateAPIView,RetrieveAPIView,AggregationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CreateAPIView.as_view(), name='call-record-list-create'),
    path('call-records/<int:pk>/',RetrieveAPIView.as_view(), name='call-record-detail'),
    path('call-records/aggregation/', AggregationAPIView.as_view(), name='call-record-aggregation'),
]