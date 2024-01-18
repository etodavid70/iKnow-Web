from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TechNews

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# class TechNewsRestView(APIView):
#   def get(self, request):
#     news=TechNews.objects.filter()
#     serializer=MathsNewsSerializer(news, many=True)
#     return render (request, 'news.html', {'all': serializer.data})
  
def TechNewsView(request):
  news=TechNews.objects.all()
  user=request.user
  cont={
    'all': news,
    'user': user,
  }
  return render(request, 'news.html', cont )
  

def login_view(request):
  if request.user.is_authenticated:
    return redirect('dashboard')
  else:
    if request.method=='POST':
      usern=request.POST['username']
      passw=request.POST['password']

      user=authenticate(request, username=usern, password=passw)

      if user is not None:
        login(request, user)
        return redirect('dashboard')
      else:
        return redirect('login')
    else:
      return render(request, 'login.html')

def logout_view(request):
  logout(request)
  return redirect('login')



def dashboard_view(request):
  if not request.user.is_authenticated:
    return redirect('login')
  else:
    return render(request, 'dashboard.html')


def signup_view(request):
  if request.method=='POST':
    form =UserCreationForm(request.POST)  
    if form.is_valid():
      user=form.save()
      login(request, user)
      return redirect('dashboard')
  else:
    form= UserCreationForm()
  return render(request, 'signup.html', {'form': form})


from django import forms
from django.db import models
from django.contrib.auth.models import User







from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import TechNewsForm
from datetime import date


def create_news_form(request):
    if not request.user.is_authenticated:
      return redirect('login')
    else:
      user = request.user
      user_name = user.username

      if request.method == 'POST':
          form = TechNewsForm(request.POST)
          if form.is_valid():
              form.save()
              return HttpResponseRedirect('success')
      else:
          
          
          initial_data = {
              'author': request.user.username, # Populate text field with the username
              'timeline': date.today(),
        }
          form = TechNewsForm(initial=initial_data)
      return render(request, 'postnews.html', {'form': form})

from .models import Like

@login_required
def success_view (request):
  return render (request, 'success.html', {})

from django.shortcuts import get_object_or_404

def star_post(request):
  user=request.user
  if request.method=='POST':
    news_id=request.POST.get('news_id')
    news_obj= TechNews.objects.get(id=news_id)

    if user in  news_obj.star.all():
      news_obj.star.remove(user)
    else:
      news_obj.star.add(user) 
    star, created= Like.objects.get_or_create(user=user, news_id=news_id)
    if not created:
      if star.value =='Star':
        star.value='Unstar'
      else:
        star.value=='Star'
    
    star.save()
  return redirect('index')