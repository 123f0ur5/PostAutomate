from django.db import models
from PostAutomate.settings import MEDIA_ROOT
from django.contrib.auth.models import User
	
# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	text = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to=MEDIA_ROOT, null=True, blank=True)
	post_date = models.DateTimeField(blank=True, null=True)
	facebook = models.BooleanField(default=False)
	instagram = models.BooleanField(default=False)
	twitter = models.BooleanField(default=False)


	def get_absolute_url(self):
		return f"/list/{self.id}"