from django.db import models


class Customer(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	work_phone = models.CharField(max_length=10, null=True, blank=True)
	home_phone = models.CharField(max_length=10, null=True, blank=True)
	email = models.EmailField(max_length=254)
	created_date = models.DateField(auto_now_add=True)
	is_archived = models.BooleanField(default=False)
	
	def __str__(self):
		return self.first_name + " " + self.last_name
	
	
class Address(models.Model):
	address1 = models.CharField(max_length=200)
	address2 = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	zip = models.IntegerField()
	customer = models.ForeignKey(Customer)
	
	def __str__(self):
		return self.address1 + " " + self.city + ", " + self.state + " " + str(self.zip)
				