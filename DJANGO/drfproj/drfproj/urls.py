from django.contrib import admin
from django.urls import path,include
from .views import GetAllPlayersView,CreateNewPlayerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('get_all_players', GetAllPlayersView.as_view(), name='test'),
    path('create_player', CreateNewPlayerView.as_view(), name='create_player'),
    path('', include('player_app.urls'))

]
