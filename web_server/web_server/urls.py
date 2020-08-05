"""web_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path

from rest_framework import routers

from .todo_api import views

# from .store_api.ressources import StoreResource
# from .store_api.urls import urlpatterns as store_api_urls

# store_ressource = StoreResource()

# from .todo_api.ressources import TodoRessource

# todo_ressource = TodoRessource

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(todo_ressource.urls)),
    # path('', include(store_api_urls)),
]

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'todo_groups', views.TodoGroupViewSet)
router.register(r'todo_items', views.TodoItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
