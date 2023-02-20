
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
class Quiz(models.Model):
    titre = models.TextField(max_length=50 ,primary_key=True)
    categorie= models.TextField(max_length=30)
    date = models.DateTimeField('date published')
    duree = models.IntegerField()
    def __str__(self):
        return self.titre
    
class Question(models.Model):
    question = models.TextField(max_length=100)
    quiz = models.ForeignKey(Quiz,on_delete=models.DO_NOTHING)
    choix1=models.TextField(max_length=50)
    choix2=models.TextField(max_length=50)
    choix3=models.TextField(max_length=50)
    reponse=models.TextField(max_length=50)
    def __str__(self):
        return self.question
    
class UserManager(BaseUserManager):

    def create_user(self, email, name,  password=None):
        """user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
          
        )
        user.set_password(password)
        user.save(using=self.db)

        return user
    def create_superuser(self, email, name,  password):
        """superuser"""
        user = self.create_user(email, name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def __str__(self):
        return self.email
class Participation(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='participation')
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE ,related_name='participation')
    score=models.IntegerField()
