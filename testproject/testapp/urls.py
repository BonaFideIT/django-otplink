from django.urls import path
from otplink.views import OTPDownloadView

urlpatterns = [
    path('otp-link/<uuid:pk>/', OTPDownloadView.as_view(), name='otp-link'),
]
