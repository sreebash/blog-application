from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'description')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == '':
            raise forms.ValidationError('Name field is required')
        return name
