# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.
import asyncio
from time import time, ctime

async def kitchen_crew():
    print(f"{ctime()} -> [Chef] puts noodle in boiling water.")
    await asyncio.sleep(1)  # Simulate a long-running operation
    print(f"{ctime()} -> [Chef] stirs the noodle.")

async def bar_crew():
    print(f"{ctime()} -> [Bartender] starts preparing a coffee bean...")
    await asyncio.sleep(1)  # Simulate a long-running operation
    print(f"{ctime()} -> [Bartender] pours espresso shot")

async def main():
    start_time = time()

    # Create tasks for both crews
    task_kitchen = asyncio.create_task(kitchen_crew())
    task_bar = asyncio.create_task(bar_crew())

    # Wait for both tasks to complete
    await task_kitchen
    await task_bar

    print(f"Total time: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop        