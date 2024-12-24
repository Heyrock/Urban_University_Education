# через multiprocessing.Queue
import datetime
import multiprocessing as mp
from queue import Empty
from PIL import Image


def resize_image(image_paths, queue):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((800, 600))
        # image.save(image_path)
        queue.put((image_path, image))


def change_color(queue):
    while True:
        try:
            image_path, image = queue.get(timeout=5)
        except Empty:
            break
        image = image.convert('L')
        image.save(image_path)


if __name__ == '__main__':
    data = []
    for num in range(1, 51):
        data.append(f'./_11_2_images/image_{num}.jpg')

    queue = mp.Queue()

    resize_pr = mp.Process(
        target=resize_image,
        args=(
            data,
            queue,
        )
    )
    change_pr = mp.Process(
        target=change_color,
        args=(
            queue,
        )
    )

    start = datetime.datetime.now()
    resize_pr.start()
    change_pr.start()

    resize_pr.join()
    change_pr.join()
    print(datetime.datetime.now() - start)

# 0:00:05.628363

# ------------------------------------------
# через multiprocessing.Pipe
import datetime
import multiprocessing as mp

from PIL import Image


def resize_image(
        image_paths,
        pipe: mp.Pipe,
        stop_event: mp.Event
):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((800, 600))
        image.save(image_path)
        pipe.send(image_path)
    stop_event.set()


def change_color(
        pipe: mp.Pipe,
        stop_event: mp.Event,
):
    while not stop_event.is_set():
        image_path = pipe.recv()
        image = Image.open(image_path)
        image = image.convert('L')
        image.save(image_path)


if __name__ == '__main__':
    data = []
    for num in range(1, 51):
        # прописывал в другой директории
        # data.append(f'../Practical_examples/_11_2_images/image_{num}.jpg')
        data.append(f'./_11_2_images/image_{num}.jpg')

    conn1, conn2 = mp.Pipe()
    stop_event = mp.Event()

    resize_pr = mp.Process(
        target=resize_image,
        args=(
            data,
            conn1,
            stop_event,
        )
    )
    change_pr = mp.Process(
        target=change_color,
        args=(
            conn2,
            stop_event,
        )
    )

    start = datetime.datetime.now()
    resize_pr.start()
    change_pr.start()

    resize_pr.join()
    change_pr.join()
    print(datetime.datetime.now() - start)

# 0:00:00.722303
