from django.db import models # type: ignore

class Users(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    last_login = models.DateTimeField(max_length=250,null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.email