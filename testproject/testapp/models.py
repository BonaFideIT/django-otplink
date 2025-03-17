from django.db import models


class TestClass(models.Model):
    name = models.CharField(max_length=100, default='test')
    file = models.FileField(upload_to='files/')
