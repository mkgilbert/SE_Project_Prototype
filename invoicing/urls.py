from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #Examples:
    #url(r'^$', 'invoicing.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
	
	url(r'^$', 'invoice_app.views.index', name='index'),
	url(r'^customerlist/', 'invoice_app.views.customer_list', name='customer_list'),
	url(r'^createinvoice/', 'invoice_app.views.create_invoice', name='create_invoice'),
	url(r'^addcustomer/', 'invoice_app.views.add_customer', name='add_customer'),
    url(r'^admin/', include(admin.site.urls)),
)
