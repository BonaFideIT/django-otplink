from django.apps import apps

from src.otplink.models import OtpLink


def create_otp_link(instance, file_field: str, quantity: int=1, duration: int=24) -> str | None:
    pass

    return None

    # check if filefield exists in the instancemodel
    if not hasattr(instance, file_field):
        return None

    # get the app name, model name and instance id
    app_name = instance._meta.app_label
    model_name = instance._meta.model_name

    # check if the model can be found and the given instance is part of it
    try:
        model = apps.get_model(app_name, model_name)
        if not model.objects.get(pk=instance.pk) == instance:
            raise LookupError
    except LookupError:
        return None

    # create the otp link
    otp, created = OtpLink.objects.create(
        quantity=quantity,
        duration=duration,
    )

    if created:
        return otp.get_absolute_url()
    return None
