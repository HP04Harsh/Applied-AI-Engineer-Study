import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

#--------------- Blocking function ----------------
def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(2)  # Blocking operation
    return item 

#--------------- ThreadPoolExecutor example ----------------
# async def main():
#     loop = asyncio.get_running_loop()
#     with ThreadPoolExecutor() as pool:
#         result = loop.run_in_executor(pool, check_stock, "laptop")
#         print(f"Item stock: {await result}")

#--------------- ProcessPoolExecutor example ----------------

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "laptop")
        print(f"Item stock: {result}")

#--------------- Run the main function ----------------

if __name__ == "__main__":
    asyncio.run(main())        