from django.http.response import HttpResponse
from django.views.generic.base import View

from .models import OtpLink, TestClass
from django_downloadview.views import ObjectDownloadView

from .functions import create_otp_link


class OTPDownloadView(ObjectDownloadView):
    """
    Serve file fields from models.
    """

    model = OtpLink


# TODO Delete me
class TestView(View):


    def get(self):
        create_otp_link(TestClass.objects.get(pk=1), 'file')
        return HttpResponse('Hello World')
