from django.contrib import admin

from models.customer import Customer, Address

admin.site.register(Customer)
admin.site.register(Address)
