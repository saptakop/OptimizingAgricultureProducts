import imp
from django.contrib import admin
from home.models import Contact
from home.models import User
from home.models import Survey

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Survey)

