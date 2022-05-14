
from django.http import    JsonResponse, Http404
from pytz import timezone
from .serializers import GameSerializer,  BetSerializer, PreviewSerializer
from .models import  Game,  Bets, Preview
import datetime
from rest_framework import viewsets
from rest_framework.response import Response

# debug_start=datetime.datetime(2022,1,1,1,1,1,1,tzinfo=timezone('US/Eastern'))
testing = False
def upcoming_matches(request):
    if testing:
        upcoming = Game.objects.filter(start_time__gt=datetime.datetime(2022,1,1,1,1,1,1,tzinfo=timezone('US/Eastern'))).filter(start_time__lt=datetime.datetime(2022,1,1,1,1,1,1,tzinfo=timezone('US/Eastern')) + datetime.timedelta(request.GET['days'])).order_by('match_id').distinct('match_id')
    else:
        upcoming = Game.objects.filter(start_time__gt=datetime.datetime.now()).order_by('match_id','start_time').distinct('match_id')
    output =[]
    
    for match in upcoming:
        output.append( 
        {'id':match.id,
        'league':match.league,
        'league_id':match.league_id,
        'preview':match.team + " vs. "+ match.opposition,
        'start_time': match.start_time}
        )

    return JsonResponse(sorted(output, key=lambda d: d['start_time']) , safe=False)


def available_leagues(request):
    days_ahead = datetime.timedelta(days=int(request.GET['days']) )if 'days' in request.GET.keys() else datetime.timedelta(days=1)
    if testing:
        upcoming = Game.objects.filter(start_time__gt=datetime.datetime(2022,1,1,1,1,1,1,tzinfo=timezone('US/Eastern'))).filter(start_time__lt=datetime.datetime(2022,1,1,1,1,1,1,tzinfo=timezone('US/Eastern')) + days_ahead).order_by('match_id').distinct('match_id')
    else:
        upcoming = Game.objects.filter(start_time__gt=datetime.datetime.now()).filter(start_time__lt=datetime.datetime(2022,1,1,1,1,1,1,tzinfo=timezone('US/Eastern')) + days_ahead).order_by('match_id').distinct('match_id')
    output =[]
    
    for match in upcoming:
        output.append( 
        {'id':match.id,
        'league':match.league,
        'league_id':match.league_id,
        'preview':match.team + " vs. "+ match.opposition,
        'date':match.start_time.date(),
        'match_id':match.match_id,
        'sport':match.sport}
        )

    return JsonResponse(sorted(output, key = lambda i: i['date']), safe=False)

def get_previews(request):
    try:
        previews = Preview.objects.all()
        serialized_data = PreviewSerializer(previews, many=True).data
    except Preview.DoesNotExist:
        raise Http404("No games upcoming")
    return JsonResponse(serialized_data, safe=False)


def get_game_preview_all(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
        # print(game.match_id)
        preview = Preview.objects.filter(match_id=game.match_id).latest('match_id')
    except Preview.DoesNotExist:
        raise Http404("No preview for this game")
    return JsonResponse([PreviewSerializer(preview).data], safe=False)

    
def get_game_preview_levels(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
        # print(game.match_id)
        preview = Preview.objects.filter(match_id=game.match_id).latest('match_id')
    except Preview.DoesNotExist:
        raise Http404("No preview for this game")
    return JsonResponse([PreviewSerializer(preview).data], safe=False)

def get_game(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("No games upcoming")
    return JsonResponse(GameSerializer(game).data)

# link to league collection too - history
def get_league(request, league_id):
    try:
        league = Game.objects.get(league_id=league_id)
    except Game.DoesNotExist:
        raise Http404("No games upcoming")
    return JsonResponse(GameSerializer(league).data)

def get_game_league(request, game_id):
    try:
        league_games = Game.objects.filter(league_id = Game.objects.get(pk=game_id).league_id)
        serialized_data = GameSerializer(league_games, many=True).data
    except Game.DoesNotExist:
        raise Http404("No preview for this game")
    return JsonResponse(serialized_data, safe=False)


def get_game_placeholder(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Preview.DoesNotExist:
        raise Http404("No preview for this game")
    return JsonResponse(GameSerializer(game).data)

def get_bets(request):
    try:
        bets = Bets.objects.all()
        serialized_data = BetSerializer(bets, many=True).data
    except Bets.DoesNotExist:
        raise Http404("No games upcoming")
    return JsonResponse(serialized_data, safe=False)

def get_strategies(request):

    return JsonResponse({"strategies":"many strategies here"}, safe=False)

def get_preferences(request):

    return JsonResponse({"preferences":"many preferences here"}, safe=False)

class BetViewSet(viewsets.ModelViewSet):
    # renderer_classes = ''
    queryset = Bets.objects.all()
    def create(self, request): # Here is the new update comes <<<<
        post_data = request.data
        Bets.objects.create(match_id=post_data['match_id'],
        line=post_data['line'],
        side=post_data['side'],
        odd=post_data['odd'],
        dollar=post_data['dollar'])

        return Response(data="return data")
    serializer_class = BetSerializer

def team_plot_venues(request,game_id ):

    return JsonResponse({"data":"lots of data"})

def team_plot_fave_dog(request,game_id ):

    return JsonResponse({"data":"lots of data"})

def team_plot_home_fave_dog(request,game_id ):

    return JsonResponse({"data":"lots of data"})

def opposition_plot_venues(request,game_id ):

    return JsonResponse({"data":"lots of data"})

def opposition_plot_fave_dog(request,game_id ):

    return JsonResponse({"data":"lots of data"})

def opposition_plot_away_fave_dog(request,game_id ):

    return JsonResponse({"data":"lots of data"})