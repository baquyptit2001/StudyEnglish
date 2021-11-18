from django.shortcuts import render
from Account.models import Profile


# Create your views here.

def home(request):
    try:
        p = Profile.objects.get(name=request.user.username)
    except Profile.DoesNotExist:
        p = None
    return render(request, 'home.html', {'p': p})


def error_404(request, exception):
    return render(request, '../templates/404.html')
