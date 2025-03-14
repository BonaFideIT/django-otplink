# django-otp-link
Generate one-time or multi-use links with expiry and temporary file management support.

## Installation
The package will be available on PyPI and can be installed using pip:
```bash
  pip install django-otp-link
```

## Usage
After installation, add `otplink` to your `INSTALLED_APPS` in your Django settings file.

you can generate a one-time link using the `generate_otp_link` function:
```python
from otplink import generate_otp_link
generate_otp_link(example_object, 'example_file_field', 1, 24)
```

The function takes the following arguments:
- `object`: The object that inherits the file
- `file_field`: The field name in the object that contains the file
- `quantity`: The number of times the link can be used
- `duration`: The expiry time in hours