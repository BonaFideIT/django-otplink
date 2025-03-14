from django.urls import path
from otplink import OTPDownloadView

urlpatterns = [
    path('otp-link/<uuid:pk>/', OTPDownloadView.as_view(), name='otp-link'),
]
