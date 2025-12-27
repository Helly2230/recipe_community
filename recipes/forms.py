from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Recipe, Comment, Rating

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full px-3 py-2 bg-gray-800/50 border border-gray-600 rounded text-white focus:outline-none focus:border-white transition-colors'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-3 py-2 bg-gray-800/50 border border-gray-600 rounded text-white focus:outline-none focus:border-white transition-colors'}),
            'password1': forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 bg-gray-800/50 border border-gray-600 rounded text-white focus:outline-none focus:border-white transition-colors'}),
            'password2': forms.PasswordInput(attrs={'class': 'w-full px-3 py-2 bg-gray-800/50 border border-gray-600 rounded text-white focus:outline-none focus:border-white transition-colors'}),
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full px-3 py-2 bg-gray-800/50 border border-gray-600 rounded text-white focus:outline-none focus:border-white transition-colors'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full px-3 py-2 bg-gray-800/50 border border-gray-600 rounded text-white focus:outline-none focus:border-white transition-colors'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'w-full px-3 py-2 bg-gray-800/50 border border-gray-600 rounded text-white focus:outline-none focus:border-white transition-colors'}),
        }

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'photo']
        widgets = {
            'photo': forms.URLInput(attrs={'class': 'w-full px-3 py-2 bg-gray-800/50 border border-gray-600 rounded text-white focus:outline-none focus:border-white transition-colors', 'placeholder': 'Enter image URL'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full px-3 py-2 neumorphism-inset text-white placeholder-gray-400', 'rows': 3, 'placeholder': 'Write your comment here...'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
        widgets = {
            'score': forms.Select(attrs={'class': 'w-full px-3 py-2 neumorphism-inset text-white'}),
        }