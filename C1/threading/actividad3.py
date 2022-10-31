"""
 Actividad:
 Crear 3 subprocesos que vivan dentro de un proceso
 1.- Descargar 5 videos simultaneos
 2.- Registrar en la base de datos por lo menos 2000 registros
 3.- Iterar un servicio 50 veces
 Deben ejecutarse de forma simultanea 
"""
import pytube
import requests
import threading
import psycopg2

try:
    conexion = psycopg2.connect(database='concurrentedb', user='postgres', password='solis2002')
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
    print("ok")
except Exception as err:
    print('Error al conecta a la base de datos')

def get_service(url):
    r = requests.get(url)
    if r.status_code == 200:
        print("datos obtenidos")
        photos = r.json()
        for photo in photos:
            write_db(photo["title"])
    print("datos guardados")	

def write_db(title):
    try:
        cursor1.execute("insert into photos (title) values ('"+title+"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexion.commit()

def download_video(url, path):
    print(f"Descargando video: {url}")
    try:
        pytube.YouTube(url).streams.first().download(path)
        print(f"Video descargado: {url}")
    except Exception as err:
        print('Error en la descarga: ', err)

def repeticiones(url_repeticion):
    response = requests.get(url_repeticion)
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
 
if __name__ == '__main__':
    urls_videos = ['https://www.youtube.com/watch?v=2llDRanO6cg&t=11s',
            'https://www.youtube.com/watch?v=MTn9lGKBteA',
            'https://www.youtube.com/watch?v=N-L49zKSQTU',
            'https://www.youtube.com/watch?v=KHZqCysq0mk',
            'https://www.youtube.com/watch?v=ua2mwzmTaFQ']
    path = "C:/Users/solop/Downloads/videos"
    url_site = "https://jsonplaceholder.typicode.com/photos"
    url_repeticion = "https://randomuser.me/api/"
    
    for x in range(0,50):
       repetir = threading.Thread(target=repeticiones, args=[url_repeticion])
       repetir.start()
       
    th_service = threading.Thread(target=get_service, args=[url_site])
    th_service.start()
    
    for url in urls_videos:
        thread_videos = threading.Thread(target=download_video, args=[url, path])	
        thread_videos.start()
    

