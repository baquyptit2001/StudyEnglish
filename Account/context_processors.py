from .models import Profile


def get_profile(request):
    try:
        profile = Profile.objects.get(name=request.user.username)
    except Profile.DoesNotExist:
        profile = None
    return {'profile': profile}
