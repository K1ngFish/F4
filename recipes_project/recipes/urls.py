# recipes/urls.py
from django.urls import path
from .views import CategoryList, RecipeList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
]
