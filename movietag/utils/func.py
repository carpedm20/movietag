from account.models import Account
from django.contrib.auth.models import User

def get_account_from_user(user):
    try:
        return Account.objects.get(user=user)
    except:
        return None

def get_account_from_usernme(username):
    try:
        user = Account.objects.get(username=username)
        return Account.objects.get(user=user)
    except:
        return None

