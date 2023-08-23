from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.forms import UserCreationForm 
# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    subjects = models.ManyToManyField(Subject)  # Remove related_name

    def __str__(self):
        return self.teacher.username




class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    STRAND_CHOICES = [
        ('STEM', 'STEM'),
        ('HUMMS', 'HUMMS'),
        ('ABM', 'ABM'),
    ]
    GRADE_CHOICES = [
        ('11', '11'),
        ('12', '12'),
    ]
    strand = models.CharField(max_length=10, choices=STRAND_CHOICES)
    grade_level = models.CharField(max_length=2, choices=GRADE_CHOICES)

    def __str__(self):
        return self.user.username




class Category(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    def __str__(self):
        return self.title

