import uuid
from django.db import models
from django.urls import reverse


# Create your models here.


class OtpLink(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    app_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    instance_id = models.IntegerField()
    file_field = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    duration = models.IntegerField(default=24)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('otp-link', kwargs={'pk': self.pk})


class TestClass(models.Model):
    name = models.CharField(max_length=100, default='test')
    file = models.FileField(upload_to='files/')
