
from django.contrib import admin

from .models import Adderess, Contact, Parent, Person

# Register your models here.
admin.site.register(Person)
admin.site.register(Parent)
admin.site.register(Adderess)
admin.site.register(Contact)
