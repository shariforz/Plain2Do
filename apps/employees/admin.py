from django.contrib import admin

from .models import Employee


#admin.site = MyAdminSite(name='myadmin')
admin.site.register(Employee)

admin.site.site_header = "Plain2Do Admin"
admin.site.site_title = "Plain2Do Admin Portal"
admin.site.index_title = "Добро пожаловать в Plain2Do"

