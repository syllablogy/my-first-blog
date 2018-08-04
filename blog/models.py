from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.user', on_delete=models.CASCADE, verbose_name='Auteur')
	title = models.CharField(max_length=200)
	text = models.TextField('article')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
	 	self.published_date = timezone.now() 
	 	self.save()
	
	def __str__(self):
		return self.title




# Create your models here.
