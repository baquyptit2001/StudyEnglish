from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def error_404(request, exception):
    return render(request, '../templates/404.html')
