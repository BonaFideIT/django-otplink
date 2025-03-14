import uuid
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class OtpObject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    file_field = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    duration = models.IntegerField(default=24)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'otplink'
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def get_absolute_url(self):
        return reverse('otp-link', kwargs={'pk': self.pk}) # todo make viewname configurable


