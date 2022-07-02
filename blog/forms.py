from django import forms
from .models import Comment, Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'feature_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Description here'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'description')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == '':
            raise forms.ValidationError('Name field is required')
        return name
