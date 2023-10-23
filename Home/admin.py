from django.contrib import admin
from .models import Contact, Organisation, User, Job

# Register your models here.

admin.site.register(Contact)
admin.site.register(Job)
admin.site.register(User)
admin.site.register(Organisation)
