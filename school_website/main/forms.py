from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Student, Post
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    strand = forms.ChoiceField(choices=Student.STRAND_CHOICES)
    grade_level = forms.ChoiceField(choices=Student.GRADE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'strand', 'grade_level']

class PostForm(forms.ModelForm):
    def __init__(self, teacher, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = teacher.subjects.all()

    class Meta:
        model = Post 
        fields = ('subject', 'title', 'body')
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
