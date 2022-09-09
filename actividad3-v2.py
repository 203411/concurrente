"""
Crear 3 subprocesos dentro de un proceso:
1. Registrar 5000 datos en la base de datos
2. Iterar un servicio 50 veces
3.- Descargar 5 videos
"""
import requests
import threading
import psycopg2
import time
import pytube

try:
    conexion = psycopg2.connect(database='concurrentedb', user='postgres', password='solis2002')
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
except Exception as err:
    print('Error al conecta a la base de datos')

def service_uno(th1_args):
    get_service(th1_args[0])

def get_service(url):
    init_time = time.time()
    r = requests.get(url)
    photos = r.json()
    for photo in photos:
        write_db(photo["title"])
    end_time = time.time() - init_time
    print(f"Hilo 1 terminado en {end_time} ms")

def write_db(title):
    try:
        cursor1.execute("insert into photos (title) values ('"+title+"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexion.commit()

def service_dos(th2_args):
    init_time = time.time()
    for _ in range(0,50):
        thread2_2 = threading.Thread(target=get_service2, args=[th2_args])
        thread2_2.start()
    end_time = time.time() - init_time
    print(f"Hilo 2 terminado en {end_time} ms")

def get_service2(th2_args):
    response = requests.get(th2_args[0])
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)

def service_tres(urls,path):
    init_time = time.time()
    for url in urls:
        thread3_2 = threading.Thread(target=get_service3, args=[url,path])
        thread3_2.start()
    end_time = time.time() - init_time
    print(f"Hilo 3 terminado en {end_time} ms")

def get_service3(url,path):
    print(f"Descargando video: {url}")
    try:
        pytube.YouTube(url).streams.first().download(path)
        titleyt = pytube.YouTube(url).title
        print(f"Video descargado: {titleyt}\nURL: {url}\n")
    except Exception as err:
        print('Error en la descarga: ', err)

if __name__ == "__main__":
    # user = "elvat"
    user = "solop"
    th1_args = ["https://jsonplaceholder.typicode.com/photos"]
    th2_args = ["https://randomuser.me/api"]
    urls_videos = ['https://www.youtube.com/watch?v=2llDRanO6cg&t=11s',
            'https://www.youtube.com/watch?v=MTn9lGKBteA',
            'https://www.youtube.com/watch?v=N-L49zKSQTU',
            'https://www.youtube.com/watch?v=KHZqCysq0mk',
            'https://www.youtube.com/watch?v=ua2mwzmTaFQ']
    path = "C:/Users/"+user+"/Downloads/videos"
    thread1 = threading.Thread(target=service_uno, args=[th1_args])
    thread2 = threading.Thread(target=service_dos, args=[th2_args])
    thread3 = threading.Thread(target=service_tres, args=[urls_videos, path])
    thread1.start()
    thread2.start()
    thread3.start()