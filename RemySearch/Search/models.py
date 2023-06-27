from django.db import models

# Create your models here.
class ArchivoPDF(models.Model):
    id = models.AutoField(primary_key=True)
    archivo = models.FileField(upload_to='pdf')

# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .utils import index_pdf_to_solr

# class PDFDocument(models.Model):
#     title = models.CharField(max_length=100)
#     pdf_file = models.FileField(upload_to='pdf_files/')

# @receiver(post_save, sender=PDFDocument)
# def index_pdf(sender, instance, created, **kwargs):
#     if created:
#         # Nuevo documento guardado, indexarlo en Solr
#         document_id = str(instance.id)
#         pdf_path = instance.pdf_file.path
#         index_pdf_to_solr(pdf_path, document_id)