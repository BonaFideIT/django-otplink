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
        # todo: extend with other attributes configurable in ObjectDownloadView
        self.file_field = obj.file_field

        # return instance of model specified in OtpObject
        return retrieve_otp_link_instance(obj)
