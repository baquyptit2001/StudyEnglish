from django.shortcuts import render
from Account.models import Profile


# Create your views here.

def home(request):
    if not Profile.objects.filter(name=request.user.username).exists():
        profile = Profile()
        profile.image = 'avt.jpg'
        profile.name = request.user.username
        profile.save()
    return render(request, 'home.html')


def error_404(request, exception):
    return render(request, '../templates/404.html')
