import os
from pathlib import Path
from pdf2docx import Converter

def pdf_a_word(pdf_path):
    path_docs = 'Documents'
    folder_docs ='@Surgir_docx'
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]
    url_descaga_docs = str(Path.home() / path_docs)
    os.makedirs(url_descaga_docs +'/'+folder_docs, exist_ok=True)

    # Ruta donde se guardará el archivo Word
    docx_path = os.path.join(url_descaga_docs,folder_docs, f'Asurgir-{file_name}.docx')
    

    # Crear un objeto de conversión
    cv = Converter(pdf_path)

        # Convertir el archivo PDF a Word
    cv.convert(docx_path, start=0, end=None)

            # Cerrar el objeto de conversión
    cv.close()
    
# pdf_a_word('cotizacion.pdf')