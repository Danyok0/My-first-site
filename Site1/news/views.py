from django.shortcuts import render
from .models import Articles

def news_home(request):
   #news1234 = Articles.objects.all()
    return render(request, 'news/news_home.html')