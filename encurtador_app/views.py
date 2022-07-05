from django.shortcuts import render
import bitly_api
# Create your views here.
def index(request):
    return render(request, 'index.html')

def shorten_url(url):
    Access_Token = 'b19834c79cd46f7e3ebdaa5a131e32a9e3ae6d1e'
    connection = bitly_api.Connection(access_token=Access_Token)
    shorten_url = connection.shorten(url)
    return shorten_url['url']

def result(request):
    if request.method == 'POST':
        url = request.POST.get('url')
    return render(request, 'result.html', {'shorten_url': shorten_url(url)})
