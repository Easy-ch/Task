from django.shortcuts import render,redirect,reverse 
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.

# Создаем отображение пользователя
def profile_view(request):
    return render(request,'app_auth/profile.html')
# Создаем аутентификацию пользователя
def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
    else:
        return render(request,'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    # проверка, что комбинация логина и пароля нашлась
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    # если не нашлась - пользователь не найден
    return render(request,'app_auth/login.html',{'error':'Пользователь не найден'})
# Создаем регистрацию пользователя
def register_view(request): 
    redirect_url = reverse('profile')
    if request.POST == 'POST': 
        form = UserCreationForm()
        if form.is_valid(): 
            form.save() 
            return redirect(redirect_url)
    else: 
        form = UserCreationForm()
        context = { 
        'error':'Неккоректное заполение'
        } 
    return render(request, 'app_auth/register.html', context) 



