from django.contrib import admin
from .models import OtpObject

# Register your models here.
admin.site.register(OtpObject)

# todo Delete Me
from .models import TestClass
admin.site.register(TestClass)
