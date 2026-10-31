import threading
import queue
import time

trabajos = queue.Queue()
lock = threading.Lock()

for doc_id in range(1, 25):
    trabajos.put(doc_id)


def trabajador(nombre):
    for _ in range(6):
        try:
            doc_id = trabajos.get_nowait()
        except queue.Empty:
            return

        try:
            time.sleep(0.1)

            with lock:
                print(f"{nombre} documento {doc_id}")
        finally:
            trabajos.task_done()


def main():
    hilos = []

    for numero in range(1, 5):
        hilo = threading.Thread(
            target=trabajador,
            args=(f"Trabajador-{numero}",)
        )
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()


if __name__ == "__main__":
    main()