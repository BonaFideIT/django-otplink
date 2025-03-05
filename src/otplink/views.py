from .models import OtpLink
from django_downloadview.views import ObjectDownloadView


class OTPDownloadView(ObjectDownloadView):
    """
    Serve file fields from models.
    """

    model = OtpLink
