from django import forms

from .models import Post

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'text', 'image', 'post_date', 'facebook', 'instagram', 'twitter']
		widgets = {'post_date' : DateInput()}