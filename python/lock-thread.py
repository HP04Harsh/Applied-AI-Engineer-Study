import threading
import time

counter = 0
l = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100):
        with l:
            counter += 1
            print(f"{threading.current_thread().name} increased counter to: {counter}")

t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=increment_counter)

t1.start()
t2.start()

t1.join()
t2.join()