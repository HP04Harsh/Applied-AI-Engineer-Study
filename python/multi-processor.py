from multiprocessing import Process, Queue
import time

order_names = ["Order1", "Order2", "Order3", "Order4", "Order5"]

def order_process(order_name, q):
    print("Processing Order", order_name, "...")
    q.put(order_name)
    time.sleep(2)
    print("Order", order_name, "processed.")

processes = []
q = Queue()
for i in range(len(order_names)):
    p = Process(target=order_process, args=(order_names[i], q))
    processes.append(p)


if __name__ == '__main__':
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()    

    for i in range(len(order_names)):
        order_name = q.get()
        print("Order", order_name, "has been processed.")
    print("All orders have been processed.")