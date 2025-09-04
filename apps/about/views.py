from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, world 🌍. This is our Django index page for Day1 Django Hosting!</h>")
