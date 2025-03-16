from django_downloadview.views import ObjectDownloadView
from .functions import retrieve_otp_link_instance
from .models import OtpObject


class OTPDownloadView(ObjectDownloadView):
    """
    Serve file fields from models.
    """
    model = OtpObject

    def get_object(self, queryset=None):
        # get OtpObject Instance
        obj = super().get_object(queryset)

        # overwrite ObjectDownloadView attributes from OtpObject
        self.file_field = obj.file_field
        self.basename_field = obj.basename_field
        self.encoding_field = obj.encoding_field
        self.mime_type_field = obj.mime_type_field
        self.charset_field = obj.charset_field
        self.modification_time_field = obj.modification_time_field
        self.size_field = obj.size_field

        # return instance of model specified in OtpObject
        return retrieve_otp_link_instance(obj)
