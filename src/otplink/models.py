import uuid
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.conf import settings


class OtpObject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    duration = models.IntegerField(default=24)

    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")

    file_field = models.CharField(max_length=100)
    basename_field = models.CharField(max_length=100, blank=True, null=True, default= None)
    encoding_field = models.CharField(max_length=100, blank=True, null=True, default= None)
    mime_type_field = models.CharField(max_length=100, blank=True, null=True, default= None)
    charset_field = models.CharField(max_length=100, blank=True, null=True, default= None)
    modification_time_field = models.CharField(max_length=100, blank=True, null=True, default= None)
    size_field = models.CharField(max_length=100, blank=True, null=True, default= None)

    class Meta:
        app_label = 'otplink'
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def get_absolute_url(self):
        viewname = 'otp_link'
        if hasattr(settings, "OTPLINK_VIEW"):
            viewname = settings.OTPLINK_VIEW

        return reverse(viewname, kwargs={'pk': self.pk})


