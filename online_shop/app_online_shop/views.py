from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import OnlineShop
from .forms import Advertisementform
from django.urls import reverse

# Create your views here.
def index(request):
    online_shops = OnlineShop.objects.all()
    context = {'online_shops': online_shops }
    return render(request, 'index.html', context)
def top_sellers(request):
    return render(request,'top-sellers.html')
def advertisement_post(request):
    if request.method == 'POST':
        form = Advertisementform(request.POST,request.FILES)
        if form.is_valid():
            advertisement = OnlineShop(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = Advertisementform()
    context = {'form':form}
    return render(request, 'advertisement-post.html',context)
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')



