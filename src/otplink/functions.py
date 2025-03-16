from datetime import timedelta
from django.utils import timezone
from django.http.response import Http404
from .models import OtpObject


def create_otp_link(instance, file_field: str, quantity: int=1, duration: int=24):
    # check if filefield exists in the instancemodel
    if not hasattr(instance, file_field):
        raise AttributeError(f'{instance.__class__.__name__} has no attribute {file_field}')

    # create the otp link
    otp = OtpObject.objects.create(
        content_object=instance,
        file_field=file_field,
        quantity=quantity,
        duration=duration,
    )

    return otp

def retrieve_otp_link_instance(otp_object) -> object:
    # check if instance can be retrieved
    if (
        otp_object.quantity < 1 # usage maximum is exceeded
        or timezone.now() > otp_object.created_at + timedelta(hours=otp_object.duration) # duration is exceeded
        or otp_object.content_object is None # instance is deleted
    ):
        raise Http404

    # decrement quantity
    otp_object.quantity -= 1
    otp_object.save()

    # return instance of the model
    return otp_object.content_object
