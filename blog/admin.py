from django.contrib import admin
from django.contrib.auth.models import User


from .models import Notice
from .models import Contact
# Register your models here.
admin.site.register(Notice)
admin.site.register(Contact)