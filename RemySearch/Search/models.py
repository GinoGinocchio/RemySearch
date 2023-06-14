from django.db import models

# Create your models here.
class ArchivoPDF(models.Model):
    id = models.AutoField(primary_key=True)
    archivo = models.FileField(upload_to='pdf')