from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from . import views



router = routers.DefaultRouter()

router.register('bets', views.BetViewSet, basename='bets')

urlpatterns = [
    path('upcoming', views.upcoming_matches, name='upcoming'),
    path('game/<int:game_id>/', views.get_game, name='get_game'),
    path('game/<int:game_id>/preview', views.get_game_preview, name='get_game_preview'),
    path('game/<int:game_id>/placeholder', views.get_game_placeholder, name='get_game_placeholder'),
    path('game/<int:game_id>/league', views.get_game_league, name='get_game_league'),

    path('bets/',views.get_bets, name='get_bets'),
    path('strategies/',views.get_strategies, name='get_strategies'),
    path('preferences/',views.get_preferences, name='get_preferences'),

    path('league/<int:league_id>/', views.get_league, name='get_league'),
    
    path('', include(router.urls)),

]