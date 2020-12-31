from django import forms
from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Post', 'Post', css_class='btn-primary'))

    class Meta:
        model = Post
        fields = [
            'photo',
            'caption'
        ]

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)

    class Meta:
        model = Comment
        fields = [
            'content',
        ]   