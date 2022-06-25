"""django_toolkit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# import a module and a function to manage URLs for the admin site
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

# this variable includes the sets of URLs from the apps in the project
urlpatterns = [
    path('admin/', admin.site.urls), # this defines URLs for the admin site
    
    # for this to work, I also need to add urls.py to the learning_logs app
    path('', include('learning_logs.urls')), # this sets the base url to the homepage of learning_logs
]
