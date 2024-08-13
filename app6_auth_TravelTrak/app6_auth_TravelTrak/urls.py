"""
URL configuration for app6_auth_TravelTrak project.

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travel.urls'), name= 'travel'),
    # django recommends to use `accounts/` as the path
    # `django.contrib.auth` is a pre-installed django app; you could fine it in `INSTALLED_APPS` in `settings.py`
    path('accounts/', include('django.contrib.auth.urls')), # this is accompanied with the urls & associated views
    path('accounts/signup/', SignupView.as_view(), name= 'signup')
]

# 'accounts/login/' [name='login'] --- we have to provide: registration/login.html
# 'accounts/logout/' [name='logout']
# 'accounts/password_change/' [name='password_change']
# ... a complete list could be find at: urls.py & views.py at django/contrib/auth directory.



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

