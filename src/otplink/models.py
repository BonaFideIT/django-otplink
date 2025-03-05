import uuid
from django.db import models
from django.urls import reverse


# Create your models here.


class OtpLink(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    file = models.FileField(upload_to='otplink')
    quantity = models.IntegerField(default=1)
    duration = models.IntegerField(default=24)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('otp-link', kwargs={'pk': self.pk})
