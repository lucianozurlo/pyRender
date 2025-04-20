from django.contrib import admin
from django.urls import path
from content.views import home, build_static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/build_static/', build_static, name='build_static'),
    path('', home, name='home'),
]
