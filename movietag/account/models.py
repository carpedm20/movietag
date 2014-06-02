from django.db import models
from django.contrib.auth.models import User

import hashlib

class Account(models.Model):
    user = models.OneToOneField(User)

    friends = models.ManyToManyField('self', symmetrical=True, null=True)

    def __unicode__(self):
        return self.user.username

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.username).hexdigest()

    def gravatar_small_url(self):
        return "http://www.gravatar.com/avatar/%s?s=20" % hashlib.md5(self.user.username).hexdigest()

    def gravatar_middle_url(self):
        return "http://www.gravatar.com/avatar/%s?s=33" % hashlib.md5(self.user.username).hexdigest()

    def account_id(self):
        return self.user.username.split('@')[0]

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
