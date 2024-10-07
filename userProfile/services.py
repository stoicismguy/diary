from .models import Profile


def get_user_profile(request_user):
    profile = Profile.objects.get(user=request_user)
    return profile