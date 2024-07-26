from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return redirect('/platform')


def platform(request):
    context = {}
    return render(request, 'third_task/platform.html', context)


def games(request):
    list_names = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {'list_names': list_names}
    return render(request, 'third_task/games.html', context)


def cart(request):
    context = {}
    return render(request, 'third_task/cart.html', context)
