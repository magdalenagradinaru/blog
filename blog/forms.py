from django import forms
from .models import Comment, Project, Technology, GalleryImage
from .models import ResearchProject


# Formular pentru comentarii
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


# Formular pentru proiecte
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'image', 'technology', 'project_file', 'score', 'complexity_status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titlu Proiect'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descriere Proiect'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Scor'}),
            'complexity_status': forms.Select(attrs={'class': 'form-control'}),
        }


# Formular pentru galeria de imagini
class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['author', 'date', 'image']
        labels = {
            'author': 'Autor',
            'date': 'Data',
            'image': 'Imagine',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume Autor'}),
        }


class ResearchProjectForm(forms.ModelForm):
    class Meta:
        model = ResearchProject
        fields = ['title', 'description', 'file']
