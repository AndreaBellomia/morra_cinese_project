from django.shortcuts                   import render
from django.http                        import HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic.list          import ListView
# Create your views here.

from .models import Game


class HomeView(ListView):
    """
    View of homepage fo strat a new game 
    context contains a list of beast 3 games 
    """

    queryset = Game.objects.all().order_by('-match_win')[0:3]
    template_name = 'game/homepage.html'
    context_object_name = "lista_sezioni"
