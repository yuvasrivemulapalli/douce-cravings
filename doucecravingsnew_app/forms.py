from django import forms
from .models import Comment

class AddItemForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    price = forms.DecimalField(label='Price')
    image = forms.ImageField(label='Image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

