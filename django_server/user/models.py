
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from user import validators
import datetime

#USERNAME_MIN_LENGTH = 5
#USERNAME_MAX_LENGTH = 20

class MyUserManager(BaseUserManager):
    def _create_generic_user(self, email, username, password, first_name, last_name, user_type):
        if not username:
            raise ValueError("Username cannot be empty")
        if not email:
            raise ValueError("Email cannot be empty")
        if not first_name:
            raise ValueError("First name cannot be empty")
        if not last_name:
            raise ValueError("Last name cannot be empty")
        if not password:
            raise ValueError("Password cannot be empty")

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            user_type=user_type,
            is_staff=user_type == 0,
            is_active=False
        )
        user.set_password(password)
        user.save(user=self._db)
        return user

    def create_user(self, email, username, password, first_name, last_name):
        return self._create_generic_user(email, username, password, first_name, last_name, 2)
        
    def create_admin(self, email, username, password, first_name, last_name):
        return self._create_generic_user(email, username, password, first_name, last_name, 0)


class MyUser(AbstractBaseUser):
    objects = MyUserManager()
    class Meta:
        db_table = 'user_entity'

    user_id = models.AutoField(primary_key=True)
    #username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True, validators=[validators.validate_username])
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    last_access = models.DateField(default=datetime.date.today)
    creation_date = models.DateTimeField(default=timezone.now)
    last_update = models.DateField(default=datetime.date.today)
    user_type = models.IntegerField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'user_type']

    def __str__(self):
        return str(self.user_id) + " (%s)" % str(self.email)

    def has_perm(self, perm, obj=None):
        return self.user_type == 0

    def has_module_perms(self, app_label):
        return True
