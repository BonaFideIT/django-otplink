from django.urls import path
from src.otplink.views import OTPDownloadView


url_patterns = [
    path('otp-link/<uuid:pk>', OTPDownloadView.as_view(), name='otp-link'),
]
