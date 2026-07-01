# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"{ctime()} -> Cooking spaghetti for customer {customer}.")
    await asyncio.sleep(1)  # Simulate a long-running operation
    print(f"{ctime()} -> Finished cooking spaghetti for customer {customer}.")


async def main():
    start_time = time()
    print(f"{ctime()} -> Starting to serve customers.")

    # Create a task for cooking spaghetti for Alice
    task_a = asyncio.create_task(cook_spaghetti("Alice"))
    print(f"{ctime()} -> main() continues to run while the task is being executed in the background.")
    

    # Wait for both tasks to complete
    await task_a

    print(f"Total time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop    

   