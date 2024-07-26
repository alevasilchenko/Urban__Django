from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return redirect('/platform')


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    list_games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {'list_games': list_games}
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')
