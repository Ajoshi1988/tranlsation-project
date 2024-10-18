from django.db import models
from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    
    ext = os.path.splitext(value.name)[1]  # Get file extension
    valid_extensions = ['.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Please upload an xlsx file.')


class UploadModel(models.Model):
    name=models.CharField(max_length=64, unique=False)
    file=models.FileField(upload_to="excel/", default='No files')
    
   


    
    