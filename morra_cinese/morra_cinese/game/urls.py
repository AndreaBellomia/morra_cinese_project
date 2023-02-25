from django.urls    import path
from game.views     import (ClosedGameView, 
                            end_game_view, game_view, home_view, 
                            game_computer_choise_json_view, get_resutl_json_view)

urlpatterns = [

    # Class Based View
    path('closegame/', ClosedGameView.as_view()),

    # function View
    path('', home_view, name='homepage'),
    path('game/<int:pk>', game_view, name='game-view'),
    path('closegame/<int:pk>', end_game_view, name='end-game-view'),

    # API Json View
    path('api-choise/', game_computer_choise_json_view, name='get-ai-play'),
    path('api-result/', get_resutl_json_view, name='get-result')
] 
