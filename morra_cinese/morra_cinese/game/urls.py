from django.urls    import path
from game.views     import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    
] 
