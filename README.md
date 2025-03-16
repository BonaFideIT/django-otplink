# django-otp-link
Generate one-time or multi-use links with expiry and temporary file management support.

- [ ] Temporary file management

## Installation
The package will be available on PyPI and can be installed using pip:
```bash
  pip install django-otp-link
```

## Usage
1. After installation, add `otplink` to your `INSTALLED_APPS` in your Django settings file.
2. extend your settings file with the following settings:
    ```python
    OTPLINK_VIEW = 'example_view'
    ```
    The `OTPLINK_VIEW` is the reverse-name of the view that will be used to reverse the one-time link.
    If not configured, the default reverse-name is `otp_link`.
3. import the generate_otp_link function and use it to generate one-time links. It returns an OtpObject object.
    ```python
    from otplink.functions import generate_otp_link
    obj = generate_otp_link(object, 'file_field', quantity, duration)
    ```
    The function takes the following arguments:
    - `object`: The object that inherits the file
    - `file_field`: The field name in the object that contains the file
    - `quantity`: The number of times the link can be used
    - `duration`: The expiry time in hours
4. The OtpObject property "get_absolute_url()" can be used to get the one-time link.
    ```python
    obj = generate_otp_link(example_object, 'example_file_field', 1, 24)
    obj.get_absolute_url()
    ```

