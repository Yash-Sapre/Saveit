from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = 'saveit'

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('api/',views.save_api),
    path('add_tags/<int:id>',views.add_tags.as_view(),name='add_tags'),
    path('search/',views.search.as_view(),name='search'),
]

