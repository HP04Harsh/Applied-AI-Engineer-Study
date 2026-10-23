import threading
import time

def order_process(order_id):
    print(f"Processing order {order_id}...")
    time.sleep(2)  # Simulate time taken to process the order
    print(f"Order {order_id} processed.")
 
# Create multiple threads to process orders concurrently
threads = []
for i in range(5):
    thread = threading.Thread(target=order_process, args=(i,),daemon=True)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All orders have been processed.")


