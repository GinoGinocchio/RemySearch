import os
import pysolr
from tika import parser
from django.conf import settings


def index_pdf_to_solr(pdf_path, document_id):
    solr = settings.SOLR_CONNECTION

    # Extraer el contenido del PDF utilizando Tika
    parsed_pdf = parser.from_file(pdf_path)
    content = parsed_pdf['content']

    # Preparar los datos para enviar a Solr
    doc = {
        'id': document_id,
        'content': content
        # Agrega otros campos según tu esquema de Solr
    }
    solr.add([doc])