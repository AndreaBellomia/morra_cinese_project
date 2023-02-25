from django.shortcuts                   import render, get_object_or_404, redirect
from django.http                        import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse, JsonResponse
from django.views.generic               import TemplateView
from django.views.generic.list          import ListView

from .forms                             import NicknameForm
from .models                            import Game
from .gameapp                           import GameApp


# external Lib
import random
import json


class ClosedGameView(TemplateView):
    """ View for render /closegame/"""

    template_name = "game/gameclosed.html"


def home_view(request):
    """ Homepage view for create a now game"""

    # POST methods crate a new onject in database and retorn a key to redirect
    if request.method == 'POST':

        # Form input for a nickname of player
        form = NicknameForm(request.POST)

        # Validate form
        if form.is_valid():

            # Get data and create a instace for db
            username = form.cleaned_data['username']
            instace = Game(
                user_name = username,
                match_win = 0,
                match_tie = 0,
                match_lost = 0,
            )

            # Push instace in db
            instace.save()

            #redirect page to a current game
            return HttpResponseRedirect(f'game/{instace.pk}')
        
    # First connection return a form
    else:
        form = NicknameForm()
    return render(request, 'game/homepage.html', {'form': form})


def game_view(request, pk):
    ''' 
    View della UserPorfile page del sito 
    '''

    queryset = Game.objects.get(pk=pk)

    if queryset.closed_game == False:
        context = {'queryset': queryset}
    
    else:
        return HttpResponseRedirect('/closegame')
    return render(request, "game/game.html", context)


def end_game_view(request, pk):
    """
    Close a current game
    """

    if request.method == 'POST': 
        
        # Get a game from Db
        instace = Game.objects.get(pk=pk)
        instace.closed_game = True
        instace.save()

    # Redirect to Home
    return redirect('/')


def game_computer_choise_json_view(request):
    """ view for return a random choise of computer """

    result = random.choice(('aiChoiceRock', 'aiChoicePaper', 'aiChoiceScissor'))
    return JsonResponse({'choice': result})


def get_resutl_json_view(request):
    """ view for register a result in db """

    if request.method == 'POST': 

        # Get a body json from a http POST
        response = json.loads(request.body)
        

        instace = Game.objects.get(pk=response['game'])

        str_game = ''

        #Converiosn patter for a GameApp Class
        conversion = {
            'umanChoiceRock': 'Rock',
            'umanChoicePaper': 'Paper',
            'umanChoiceScissor': 'Scissor',
            'aiChoiceRock': 'Rock',
            'aiChoicePaper': 'Paper',
            'aiChoiceScissor': 'Scissor',
        }

        # Call a class for get a result 
        game = GameApp(response['player'], response['computer'], conversion).get_win()


        # Update a Db Game 
        if game == 1:
            instace.match_win = instace.match_win + 1
            str_game = 'Hai Vinto'
        elif game == 0:
            instace.match_lost = instace.match_lost + 1
            str_game = 'Hai Perso' 
        elif game == 2:
            instace.match_tie = instace.match_tie + 1
            str_game = 'Hai Pareggiato' 

        instace.save()
    
        # define the context to return as a response
        context = {
            'win': instace.match_win,
            'tie': instace.match_tie,
            'lost': instace.match_lost,
            'str': str_game
            }
    else:
        context = None
    return JsonResponse(context)

