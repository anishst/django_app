from django import forms
from blog.models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields from form
        fields = ('title', 'author', 'category', 'body', 'favorite')

        widgets = {
            # pass css classes for bootstrap
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'favorite': forms.CheckboxInput(),
        }
        # customize form field labels
        labels = {
            'favorite': 'Mark this favorite?'
        }