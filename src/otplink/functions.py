from datetime import datetime, timedelta

from django.apps import apps
from django.http.response import Http404

from .models import OtpObject


def create_otp_link(instance, file_field: str, quantity: int=1, duration: int=24) -> str | None:
    # check if filefield exists in the instancemodel
    if not hasattr(instance, file_field):
        return None

    # get the app name and model name
    app_name = instance._meta.app_label
    model_name = instance._meta.model_name

    # check if the model can be found and the given instance is part of it
    model = apps.get_model(app_name, model_name)
    if not model.objects.get(pk=instance.pk) == instance:
        raise LookupError

    # create the otp link
    otp = OtpObject.objects.create(
        app_name=app_name,
        model_name=model_name,
        instance_id=instance.pk,
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

    # decrement quantity
    otp_object.quantity -= 1
    otp_object.save()

    # return instance of the model
    return apps.get_model(otp_object.app_name, otp_object.model_name).objects.get(pk=otp_object.instance_id)
