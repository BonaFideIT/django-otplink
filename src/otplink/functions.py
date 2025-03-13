from datetime import datetime, timedelta
from django.http.response import Http404
from .models import OtpObject


def create_otp_link(instance, file_field: str, quantity: int=1, duration: int=24) -> str | None:
    # check if filefield exists in the instancemodel
    if not hasattr(instance, file_field):
        return None

    # create the otp link
    otp = OtpObject.objects.create(
        content_object=instance,
        file_field=file_field,
        quantity=quantity,
        duration=duration,
    )

    return otp.get_absolute_url()

def retrieve_otp_link_instance(otp_object: OtpObject):
    # check if instance can be retrieved
    if otp_object.quantity < 1:
        raise Http404
    if datetime.now() > otp_object.created_at + timedelta(hours=otp_object.duration):
        raise Http404
    if otp_object.content_object is None:
        raise Http404

    # decrement quantity
    otp_object.quantity -= 1
    otp_object.save()

    # return instance of the model
    return otp_object.content_object
