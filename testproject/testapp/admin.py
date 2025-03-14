# utils
from django.contrib import admin
from django.urls import path
from django.urls.base import reverse
from django.utils.html import format_html
from django.http.response import HttpResponse

# models
from .models import TestClass
from otplink import OtpObject

# functions
from otplink import create_otp_link


@admin.register(TestClass)
class TestClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'otp_links', 'add_otp_link')
    readonly_fields = ('otp_links','add_otp_link',)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('create-otp-link/<int:pk>/<int:quantity>/<int:duration>/', self.create_otp_link, name='create_otp_link'),
        ]
        return my_urls + urls

    def create_otp_link(self, request, pk, quantity=1, duration=24):
        obj = TestClass.objects.get(pk=pk)
        create_otp_link(obj, 'file', quantity, duration)

        return HttpResponse()

    def otp_links(self, obj):
        links = OtpObject.objects.filter(object_id=obj.pk)
        return format_html('<br>'.join([f'<a href="{link.get_absolute_url()}">{link.content_object.name}</a>' for link in links]))


    def add_otp_link(self, obj):
        return format_html('<a href="{}">Generate otp link</a>', reverse('admin:create_otp_link', args=[obj.pk]))


