from django.contrib import admin
from django.urls import path,include
from .views import CustomAuthTokenLogin, GetAllPlayersView,CreateNewPlayerView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('get_all_players', GetAllPlayersView.as_view(), name='test'),
    path('create_player', CreateNewPlayerView.as_view(), name='create_player'),
    path('', include('player_app.urls')),
    #path('api/token/', obtain_auth_token, name='get_token')
    path('api-token-auth/', CustomAuthTokenLogin.as_view())
]
