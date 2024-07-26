from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['user1', 'user2', 'user3']


def check_errors(username, password, repeat_password, age):
    result = None
    if password != repeat_password:
        result = 'Пароли не совпадают!'
    elif int(age) < 18:
        result = 'Вам должно быть не меньше 18 лет!'
    elif username in users:
        result = 'Пользователь уже существует!'
    return result


def sign_up_by_html(request):
    representation = 'HTML'
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        error = check_errors(username, password, repeat_password, age)
        if not error:
            return HttpResponse(f'<center><h2 style=color:Green>Приветствуем, {username}!</h2></center>')
    info = {'representation': representation, 'error': error}
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    representation = 'Django'
    error = None
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            error = check_errors(username, password, repeat_password, age)
            if not error:
                return HttpResponse(f'<center><h2 style=color:Green>Приветствуем, {username}!</h2></center>')
    else:
        form = UserRegister()
    info = {'representation': representation, 'error': error, 'form': form}
    return render(request, 'fifth_task/registration_page.html', info)
