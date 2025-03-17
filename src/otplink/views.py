from django.http.response import Http404
from django_downloadview.views import ObjectDownloadView
from .models import OtpObject
from django.utils import timezone
from datetime import timedelta


class OTPDownloadView(ObjectDownloadView):
    """
    Serve file fields from models.
    """
    model = OtpObject
    base_object = None

    def get_queryset(self):
        return super().get_queryset().filter(quantity__gt=0)


    def get_object(self, queryset=None):
        # get OtpObject Instance
        self.base_object = super().get_object(queryset)

        # check if instance can be retrieved
        if self.base_object.created_at + timedelta(hours=self.base_object.duration) < timezone.now():
            raise Http404

        # overwrite ObjectDownloadView attributes from OtpObject
        self.file_field = self.base_object.file_field
        self.basename_field = self.base_object.basename_field
        self.encoding_field = self.base_object.encoding_field
        self.mime_type_field = self.base_object.mime_type_field
        self.charset_field = self.base_object.charset_field
        self.modification_time_field = self.base_object.modification_time_field
        self.size_field = self.base_object.size_field

        # return instance of model specified in OtpObject
        if self.base_object.is_foreign_object():
            return self.base_object.content_object
        return self.base_object

    def get(self, request, *args, **kwargs):
        res = super().get(request, *args, **kwargs)

        # cleanup OtpObject
        if self.base_object.quantity == 1:
            self.base_object.delete()
        else:
            self.base_object.quantity -= 1
            self.base_object.save()

        return res

