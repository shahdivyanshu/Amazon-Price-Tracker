from django.db import models
from .utils import get_link_data
# Create your models here.
class Link(models.Model):
	name=models.CharField(max_length=220,blank=True)
	url=models.URLField()
	current_price=models.FloatField(blank=True)
	old_price=models.FloatField(blank=True)
	difference=models.FloatField(blank=True)
	updated=models.DateTimeField(auto_now=True)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering=('difference','-created')

	def save(self,*args,**kwargs):
		name,price=get_link_data(self.url)
		old_price=self.current_price
		if self.current_price:
			if price!=old_price:
				self.old_price=self.current_price
				self.current_price=price
				self.difference=round(self.current_price-self.old_price,2)

		else:
			self.old_price=0
			self.difference=0
		self.current_price=price
		self.name=name
		super().save(*args,**kwargs)
