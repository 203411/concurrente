
import requests
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
                                                               
if __name__ == '__main__':
    url_site = "https://jsonplaceholder.typicode.com/photos"
    for x in range(0,500000):
        print("Vuelta: ", x)
        get_service(url_site)