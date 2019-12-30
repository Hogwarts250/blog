from django import forms

from .models import Topic, Post

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["topic", "text"]
        labels = {"topic":"" , "text": ""}