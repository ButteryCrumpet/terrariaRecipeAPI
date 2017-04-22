from django.conf.urls import url

from recipeAPI import views

app_name = 'recipeAPI'
urlpatterns = [
    url(r'^recipes/(?P<pk>[a-z_]+)/$', views.RecipeDetail.as_view(), name='recipe_detail'),
    url(r'^items/(?P<pk>[a-z_]+)/$', views.ItemDetail.as_view(), name='item_detail'),
    url(r'^items/$', views.ItemList.as_view(), name='item_list'),
    url(r'^items/search/(?P<search_term>[a-z]+)/$', views.ItemSearch.as_view(), name='item_search'),
    url(r'^manager/item/(?P<pk>[a-z_]+)/$', views.ItemCreate.as_view(), name='item_create'),
    url(r'^manager/recipe/(?P<pk>[a-z_]+)/$', views.RecipeCreate.as_view(), name='recipe_create'),
]