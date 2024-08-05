from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db.models import Q








class email_backend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email__iexact=username))
        except User.DoesNotExist:
            return None
        except User.MultipleObjectsReturned:
            return User.objects.filter( email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        
        except User.DoesNotExist:
            return None
        else:
            return user if self.user_can_authenticate(user) else None
        