from django.db import models
from otplink.functions import create_otp_link


class TestClass(models.Model):
    name = models.CharField(max_length=100, default='test')
    file = models.FileField(upload_to='files/')

    def save(self, *args, **kwargs):
        # create otp link
        ret = super().save(*args, **kwargs)
        create_otp_link(self, 'file')

        return ret
