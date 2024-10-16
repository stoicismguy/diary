from .models import Profile, User


class UserDAL:
    @staticmethod
    def get_user_profile(request_user):
        profile = Profile.objects.get(user=request_user)
        return profile

    @staticmethod
    def get_user_by_username(username: str):
        user = User.objects.get(username=username)
        if user is None:
            raise Exception(f"Found no  user with this username: {username}")
        return user
    
    @staticmethod
    def get_user_by_uuid(uuid: str):
        user = User.objects.get(id=uuid)
        if user is None:
            raise Exception(f"Found no  user with this uuid: {uuid}")
        return user