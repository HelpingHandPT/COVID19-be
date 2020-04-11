
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password, first_name, last_name):
        if not username:
            raise ValueError("Username cannot be empty")
        if not email:
            raise ValueError("Email cannot be empty")
        if not first_name:
            raise ValueError("First name cannot be empty")
        if not last_name:
            raise ValueError("Last name cannot be empty")

        user = self.model(
            email=self.normalize_email(email)
        )


class MyUser(AbstractBaseUser):
    objects = MyUserManager()
    class Meta:
        db_table = 'user_entity'

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    last_access = models.DateField()
    creation_date = models.DateField()
    last_update = models.DateTimeField()
    user_type = models.IntegerField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'user_id'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'user_type']

    def __str__(self):
        return str(self.user_id) + " (%s)" % str(self.email)

    def has_perm(self, perm, obj=None):
        return self.user_type == 1

    def has_module_perms(self, app_label):
        return True
