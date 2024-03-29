from django.shortcuts import render, redirect
from .models import Url

# Create your views here.
def home(request):
    if request.method == "POST":
        url = request.POST.get('url')
        obj = Url.shorten(url)
        return render(request, 'home.html', {
            'url': obj.url,
            'short_url': obj.short_url,
            'short_url_link': 'tecos.cf' + '/' + obj.short_url
        })
    return render(request, 'home.html')

def route(request, pk):
    try:
        obj = Url.objects.get(short_url=pk)
        return redirect(obj.url)
    except:
        return redirect(home)