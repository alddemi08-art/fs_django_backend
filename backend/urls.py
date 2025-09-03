from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Backend is running!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # root URL test page
    path('api/contact/', include('base.urls')),  # your API endpoint
]
