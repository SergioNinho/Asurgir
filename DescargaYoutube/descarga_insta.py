import instaloader
import requests
import os
from pathlib import Path

def bajar_insta(link):
    # Crear una instancia de Instaloader
    L = instaloader.Instaloader()

    # URL del reel de Instagram
    reel_url = link

    # Obtener el post usando el shortcode
    post = instaloader.Post.from_shortcode(L.context, reel_url.split("/")[-2])
    titulo = post.title
    page_name = post.owner_username
    nombre ='Asurgir-' + page_name +'-' + titulo 
    # Extraer el URL del video MP4
    video_url = post.video_url

    # crear ruta
    path_insta = 'Videos'
    folder_insta = '@surgir.mp4'
    url_descargas_insta = str(Path.home() / path_insta)
    os.makedirs(url_descargas_insta +'/'+folder_insta, exist_ok=True)

    # Descargar el video MP4
    response = requests.get(video_url)
    with open(os.path.join(url_descargas_insta, folder_insta,nombre +".mp4"), "wb") as file:
        file.write(response.content)

    print("Descarga completada.")
    print(page_name)

# bajar_insta('https://www.instagram.com/reel/DCfOQ3GxVfW/?utm_source=ig_web_copy_link')



