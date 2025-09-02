from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contact/', include('base.urls')),  # ← use your app name here
]
