from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, world 🌍. This is our home page for Day1 Django Hosting!</h> today was including a mysql database for mariadb server.")
