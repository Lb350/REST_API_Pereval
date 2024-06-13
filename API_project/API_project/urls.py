from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pereval import views
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'pereval', views.PerevalAddedViewset, 'PerevalAdded')
router.register(r'user', views.UserViewset, basename='User')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += doc_urls