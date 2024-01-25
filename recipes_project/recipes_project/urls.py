# recipes_project/urls.py
from django.contrib import admin
from django.urls import path, include
from recipes.views import CategoryList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recipes.urls')),
    path('', CategoryList.as_view(), name='category-list'),
]

