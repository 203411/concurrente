from threading import Semaphore, Thread
import pytube 
semaphore = Semaphore(1)

def download(id, url,path):
    print(f"Descargando video: {url}")
    try:
        pytube.YouTube(url).streams.first().download(path)
        print(f"Video descargado: {url}")
    except Exception as err:
        print('Error en la descarga: ', err)
    
def critico(id):
    global x;
    x = x + id
    print("Hilo = " + str(id) + " => " + str(x))
    
    x = 1

class Hilo(Thread):
    def __init__(self, id, url, path):
        Thread.__init__(self)
        self.id = id
        self.url = url
        self.path = path
    def run(self):
        semaphore.acquire()
        download(self.id, self.url, self.path)
        semaphore.release()
        
        
if __name__ == "__main__":
    urls_videos = ['https://www.youtube.com/watch?v=2llDRanO6cg&t=11s',
            'https://www.youtube.com/watch?v=MTn9lGKBteA',
            'https://www.youtube.com/watch?v=N-L49zKSQTU',
            'https://www.youtube.com/watch?v=KHZqCysq0mk',
            'https://www.youtube.com/watch?v=ua2mwzmTaFQ']
    path = "C:/Users/solop/Downloads/videos"

    threads_semaphores = [Hilo(1,urls_videos[0],path), Hilo(2,urls_videos[1],path), Hilo(3,urls_videos[2],path), Hilo(4,urls_videos[3],path), Hilo(5,urls_videos[4],path)]
    x = 1;
    for t in threads_semaphores:
        t.start()