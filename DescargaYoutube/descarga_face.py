import yt_dlp
import os
from pathlib import Path

def bajar_face(url):
    """
    Descarga un video de la URL proporcionada utilizando yt-dlp.

    Args:
        url (str): URL del video a descargar.
        download_folder (str): Carpeta donde se guardará el archivo descargado.

    Returns:
        str: Ruta completa del archivo descargado.
    """
    path_face = 'Videos'
    folder_face = '@surgir.mp4'
    url_descargas_face = str(Path.home() / path_face)
    # Asegurarse de que la carpeta de descargas exista
    os.makedirs(url_descargas_face +'/'+folder_face, exist_ok=True) 


    # Configuración de yt-dlp
    ydl_opts = {
        'outtmpl': f'{os.path.join(url_descargas_face, folder_face)}/Asurgir- %(title)s.%(ext)s',  # Plantilla para el nombre del archivo
        'format': 'bestvideo+bestaudio/best'             # Descargar la mejor calidad
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)  # Extraer información y descargar el video
            filename = ydl.prepare_filename(info)        # Obtener el nombre del archivo descargado
        return filename
    except Exception as e:
        raise RuntimeError(f"Error al descargar el video: {str(e)}")

# descargar_video_face('https://www.facebook.com/share/v/1CY2oy11fi/')

