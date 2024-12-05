#!/usr/local/bin/python
from flask import Flask, render_template,render_template_string, request, Response,redirect, send_file
import os
from os import remove
from pathlib import Path
# from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import time
# import aspose.words as aw
import whisper
from DescargaYoutube.you_tube import descarga_video, descarga_audio, video_texto
from DescargaYoutube.pdf_word import pdf_a_word
from DescargaYoutube.descarga_insta import bajar_insta
from DescargaYoutube.descarga_face import bajar_face
from DescargaYoutube.descargar_x import bajar_x

app = Flask(__name__)
# app.secret_key="asurgir"
# mysql= MySQL()

# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='sedasasi060904'
# app.config['MYSQL_DB']='contactanos'
# mysql.init_app(app)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/programacionweb/')
def programacionweb():
    return render_template('programacionweb.html')

@app.route('/diseñografico/')
def diseñografico():
    return render_template('diseñografico.html')

@app.route('/marketingdigital/')
def marketingdigital():
    return render_template('marketingdigital.html')

@app.route('/contactanos/')
def contactanos():
    return render_template('contactanos.html')

@app.route('/contactanos/enviar', methods=['POST', 'GET'])
def contactanos_enviar():
    if request.method=='POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telf = request.form['telf']
        tel = request.form['tel']
        pais = request.form['pais']
        comentario = request.form['comentario']
        
        sql="INSERT INTO formulario(id, nombre, email, telf, tel, pais, comentario )VALUES (NULL, %s, %s, %s,%s, %s, %s); "
        datos=(nombre, email, telf, tel, pais, comentario)
        
        cursor=mysql.connection.cursor()
        cursor.execute(sql,datos)
        mysql.connection.commit()
        cursor.close()
        
        mensaje = 'Gracias por contactarnos, pronto un asesor se contactara con ested'
        return render_template('contactanos.html',  mensaje = mensaje)

@app.route('/descarga_de_youtube/')
def descarga_de_youtube():
 
    
    return render_template('descarga_de_youtube.html')

@app.route('/descarga_de_youtube/envia', methods=['POST'])
def envia():
    if request.method == 'POST':
        url_aud = request.form['url']
        descarga_video(url_aud)  
        mensaje_2= '¡Tu descarga ha sido exitosa!'       
        return render_template('descarga_de_youtube.html', mensaje_2 = mensaje_2)
    else:
        mensaje_2 = 'Erro al descargar, url protejida' 
        return render_template('descarga_de_youtube.html', mensaje_2 = mensaje_2)
        
    

@app.route('/descarga_de_youtube/envia2', methods=['POST'])
def envia2():   
    if request.method=='POST':
        url_aud = request.form['url']
        descarga_audio(url_aud)         
        mensaje_2= '¡Tu descarga ha sido exitosa!'
        return render_template('descarga_de_youtube.html', mensaje_2 = mensaje_2)
    else:
        mensaje_2 = 'Erro al descargar, url protejida' 
        return render_template('descarga_de_youtube.html', mensaje_2 = mensaje_2)
        
@app.route('/De_PDF_a_Word/') 
def de_pdf_a_word():
   
    return render_template('De_PDF_a_WORD.html')

@app.route('/De_PDF_a_Word/envia_pdf', methods=['POST'])
def De_PDF_a_Word_envia():   
    if 'urlpdf' not in request.files: 
        return 'No file part' 
    file = request.files['urlpdf'] 
    if file.filename == '':
        return 'No selected file' 
    if file: # Guardar el archivo PDF temporalmente 
        pdf_path = os.path.join('DescargaYoutube', file.filename)
        file.save(pdf_path) # Convertir PDF a Word usando la función externa 
        pdf_a_word(pdf_path)
    time.sleep(5)
    remove(pdf_path)
    mensaje ="Has convertido el documento con exito"  
        
   
    return render_template_string(""" <script>alert('El documento se ha convertido con exito'); window.location.href=/De_PDF_a_Word/;</script> """)
      
@app.route('/video_a_texto/')
def video_a_texto():
    
    return render_template('video_a_texto.html')
    

@app.route('/video_a_texto/envia_txt', methods=['POST'])
def video_a_texto_envia():
    if request.method=='POST':
        url_txt = request.form['url_txt']
        video_texto(url_txt)
        
    # return render_template('video_a_texto.html')
    return render_template_string(""" <script>alert('El audio se ha transcrito con exito'); window.location.href=/video_a_texto/;</script> """)

@app.route('/descarga_insta/')
def descarga_insta():
    return render_template('descarga_insta.html')

@app.route('/descarga_insta/envia_insta', methods=['POST'])
def envia_insta():
    if request.method == 'POST':
        url_aud = request.form['url']
        bajar_insta(url_aud)  
        mensaje_2= '¡Tu descarga ha sido exitosa!'       
        return render_template_string(""" <script>alert('Tú video se ha descargado con exito'); window.location.href=/descarga_insta/;</script> """)
    else:
        mensaje_2 = 'Erro al descargar, url protejida' 
        return render_template('descarga_insta.html', mensaje_2 = mensaje_2)
    
@app.route('/descarga_face/')
def descarga_face():
    return render_template('descarga_face.html')

@app.route('/descarga_face/envia_face', methods=['POST'])
def envia_face():
    if request.method == 'POST':
        url_aud = request.form['url']
        bajar_face(url_aud)  
        mensaje_2= '¡Tu descarga ha sido exitosa!'       
        return render_template_string(""" <script>alert('Tú video se ha descargado con exito'); window.location.href=/descarga_face/;</script> """)
    else:
        mensaje_2 = 'Erro al descargar, url protejida' 
        return render_template('descarga_face.html', mensaje_2 = mensaje_2) 
    
@app.route('/descarga_x/')
def descarga_x():

    
    return render_template('descarga_x.html')

@app.route('/descarga_x/envia_x', methods=['POST'])
def envia_x():
    if request.method == 'POST':
        url_aud = request.form['url']
        bajar_x(url_aud)  
        mensaje_2= '¡Tu descarga ha sido exitosa!'       
        return render_template_string(""" <script>alert('Tú video se ha descargado con exito'); window.location.href=/descarga_x/;</script> """)
    else:
        mensaje_2 = 'Erro al descargar, url protejida' 
        return render_template('descarga_x.html', mensaje_2 = mensaje_2) 
        
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
