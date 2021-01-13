from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    # manipulate objects
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have and email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # the passward is encrypted we want to make sure the password
        # is coverted to a hash and never stored as plain test in the database
        user.set_password(password)
        # best practice to add this line anyway just to make sure that you
        # support multiple databases in the future
        user.save(using=self._db)

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        # is_superuser is  automatically created by the permissions mixin
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # it helps explain what the purpose of the class is that you've created
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # this is require because we need to use our custom user model with the Django CLI
    # so Django needs to have a custom model manager for the user model so it knows
    # how to create users and control users using the Django CLI tools
    objects = UserProfileManager()

    # override default username field which is normally called username
    USERNAME_FIELD = 'email'
    # this says that the username field is required by default so just by setting it
    # setting email and the username thats means that this is required and then
    # you have additional required fields and we want to say that
    # at a minimum the user must specify their email address and their name
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve shot name of user"""
        return self.name

    # A Python “magic method” that returns a string representation of any object.
    def __str__(self):
        """Return string representation of our user"""
        return self.email
