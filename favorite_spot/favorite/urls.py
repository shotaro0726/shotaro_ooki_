from django.urls import path
from .views import Favorite_Spot_View

app_name = 'favorite'

urlpatterns = [
    path('',Favorite_Spot_View.as_view(),name='favorite_spot'),
]