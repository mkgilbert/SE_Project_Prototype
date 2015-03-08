from django.shortcuts import render
from models.customer import Customer, Address
from django.forms import ModelForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib import messages


class AddCustomerForm(ModelForm):
	address1 = forms.CharField(max_length=50)
	address2 = forms.CharField(max_length=50,required=False)
	city = forms.CharField(max_length=40)
	state = forms.CharField(max_length=2)
	zip = forms.IntegerField()
	
	class Meta:
		model = Customer
		fields = ('first_name',
				  'last_name',
				  'home_phone',
				  'work_phone',
				  'email',
				  )
		

def index(request):
	return render(request, 'index.html', {})

def add_customer(request):
	if request.method == 'POST':
		form = AddCustomerForm(request.POST)
		if form.is_valid():
			messages.success(request, "New Customer added successfully")
			# save the Customer model info
			new_customer = form.save()
			# get the Customer object that we just created
			new_customer = Customer.objects.latest('id')
			# create a new address and tie it to that new Customer
			Address.objects.create(
				address1 = form.cleaned_data['address1'],
				address2 = form.cleaned_data['address2'],
				city = form.cleaned_data['city'],
				state = form.cleaned_data['state'],
				zip = form.cleaned_data['zip'],
				customer = new_customer
			)
			return HttpResponseRedirect('/addcustomer/')
	elif request.method == 'GET':
		form = AddCustomerForm()
	else:
		return HttpResponseRedirect('/addcustomer/')
	return render(request, 'add_customer.html', {'form': form})
			
def customer_list(request):
	customers = Customer.objects.all()
	return render(request, 'customer_list.html', { 'customers': customers })
	
def create_invoice(request):
	pass
	