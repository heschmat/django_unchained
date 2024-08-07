"""
URL configuration for app2_templates project.

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

from movies.views import home, top_movies


"""
NOTE: 
When the user visits `favorites/` django redirects it to the `top_movies()` view.
Now, if inside our app, we want to redirect to the `top_views()` we will use the `name` corresponding to the `path`
For example:
    <a href="{% url 'top-movies' %}">TopMovies</a>
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),
    path('favorites/', top_movies, name= 'top-movies'),
]
