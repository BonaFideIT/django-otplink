from django.urls import path
from src.otplink.views import OTPDownloadView, TestView

url_patterns = [
    path('otp-link/<uuid:pk>', OTPDownloadView.as_view(), name='otp-link'),

    # todo delete me
    path ('', TestView.as_view(), name='test-view'),
]
