"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from store.views import BookViewSet, auth, UserBookRelationView
from django.contrib.auth.views import LogoutView

router = SimpleRouter()

router.register('book', BookViewSet)
router.register('book_relation', UserBookRelationView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path('map/', MapView.as_view(), name='map_list')

]

urlpatterns += router.urls
