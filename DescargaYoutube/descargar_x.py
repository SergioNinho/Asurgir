import yt_dlp
import os
from pathlib import Path
    

def bajar_x(url):
    """
    Descarga un video desde una URL de X (antes Twitter) usando yt-dlp con un nombre de archivo específico.

    Args:
        url (str): URL del video o tweet que contiene el video.
        nombre_archivo (str): Nombre del archivo de salida (con extensión).

    Returns:
        str: Ruta completa del archivo descargado.
    """

    path_x = 'Videos'
    folder_x = '@surgir.mp4'
    url_descargas_x = str(Path.home() / path_x)
    # nombre_archivo = f'Asurgir-Descarga-x.mp4'
    # Asegurarse de que la carpeta de descargas exista
    os.makedirs(url_descargas_x +'/'+folder_x, exist_ok=True) 
    # Configuración de yt-dlp para replicar el comando del terminal
    # ydl_opts = {
    #     'outtmpl':f'{os.path.join(url_descargas_face, folder_face)}/Asurgir-Descarga-x.%(ext)s' ,  # Configuración del nombre del archivo
    #     'format': 'best',          # Descargar la mejor calidad disponible
    # }

    ydl_opts = {
        'format': 'best',  # Descargar la mejor calidad disponible
        'quiet': True,     # Desactiva mensajes en la consola
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extraer información del video (sin descargar)
        info = ydl.extract_info(url, download=False)

        # Obtener título    
        titulo = info.get("title", "video_sin_titulo")
        extension = info.get("ext", "mp4")  # Extensión predeterminada (mp4)

        # Determinar el nombre del archivo
        
        nombre_archivo = f"{titulo}.{extension}"
        print(nombre_archivo)
        if len(nombre_archivo) > 40:
        # Actualizar la plantilla de salida
            ydl_opts['outtmpl'] =f'{os.path.join(url_descargas_x, folder_x)}/Asurgir-{nombre_archivo[0:20]}....mp4'
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Descargar el video
                    ydl.download([url])
            # return nombre_archivo
            except Exception as e:
                raise RuntimeError(f"Error al descargar el video: {e}")
        elif len(nombre_archivo) <= 40:
            ydl_opts['outtmpl'] =f'{os.path.join(url_descargas_x, folder_x)}/Asurgir-{nombre_archivo}'
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Descargar el video
                    ydl.download([url])
            # return nombre_archivo
            except Exception as e:
                raise RuntimeError(f"Error al descargar el video: {e}")
        
        



# bajar_x("https://x.com/MariaFdaCabal/status/1859920721650069714")