from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_email", "comment_text"]

    user_email = forms.CharField(label="Your Email:", widget= forms.EmailInput(attrs={"class": "form-control"}))
    comment_text = forms.CharField(label="Your Comment:", widget=forms.Textarea(attrs={"class": "form-control"}))