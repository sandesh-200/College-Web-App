from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from blog.models import Student

from .models import Notice
from .models import Contact
# Register your models here.
admin.site.register(Notice)
admin.site.register(Contact)

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'

class UserAdmin(BaseUserAdmin):
    inlines = [StudentInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)