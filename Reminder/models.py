from django.db import models

class List(models.Model):
	category = models.CharField(max_length=200)
	
	def __unicode__(self): 
		return self.category

class category(models.Model):
	reminder = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self): 
		return self.reminder

	def __unicode__(self): 
		return self.pub_date


