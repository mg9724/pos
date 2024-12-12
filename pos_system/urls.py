"""
URL configuration for pos_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse  # Import HttpResponse

# Add a simple view to handle requests to the root URL
def home(request):
    return HttpResponse("Welcome to the home page!")  # Simple response for the homepage

urlpatterns = [
    path('', home, name='home'),  # This handles requests to '/'
    path('admin/', admin.site.urls),
    path('api/', include('restaurant.urls')),
]

