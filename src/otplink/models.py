import uuid
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.db.utils import IntegrityError
from django.urls import reverse
from django.conf import settings


class OtpObject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    duration = models.IntegerField(default=24)

    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    content_object = GenericForeignKey("content_type", "object_id")
    file_object = models.FileField(upload_to="otplink", null=True, blank=True) # todo: make upload path configurable

    file_field = models.CharField(max_length=100, blank=True, null=True, default="file_object")
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

    def save(self, *args, **kwargs):
        """
        Save method that will run clean and convert any validation errors into integrity errors
        """

        try:
            self.clean()
        except ValidationError as e:
            raise IntegrityError(e)
        super().save(*args, **kwargs)

    def is_foreign_object(self):
        return self.content_object is not None

    def get_absolute_url(self):
        viewname = 'otp_link'
        if hasattr(settings, "OTPLINK_VIEW"):
            viewname = settings.OTPLINK_VIEW

        return reverse(viewname, kwargs={'pk': self.pk})

    # todo: test clean function
    def clean(self):
        if self.content_object is None or self.file_object is None:
            raise ValidationError("Instance is deleted")
        if self.content_object and self.file_object:
            raise ValidationError("content_object and file_object are mutually exclusive")
        if self.file_object and self.file_field != "file_object":
            raise ValidationError("file_field must be 'file_object' if file_object is set")
        if self.content_object and not hasattr(self.content_object, str(self.file_field)):
            raise ValidationError(f"content_object has no attribute '{self.file_field}'")
