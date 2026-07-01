# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} ->Cooking for {name}.")
    await asyncio.sleep(1)  # Simulate a long-running operation
    print(f"{ctime()} ->Finished cooking for {name}.")

async def main():
    start_time = time()
    print(f"{ctime()} -> Starting to serve customers.")

    await serve_customer("Alice")
    await serve_customer("Bob")


    print(f"Total time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop       