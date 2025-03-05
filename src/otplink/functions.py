from typing import Any

from django.core.files import File
from src.otplink.models import OtpLink


def create_otp_link(file: File, quantity: int=1, duration: int=24) -> str | None:
    otp, created = OtpLink.objects.create(
        file=file,
        quantity=quantity,
        duration=duration,
    )

    if created:
        return otp.get_absolute_url()
    return None
