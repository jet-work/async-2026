# Program 4: The await Keyword
# Concept: Pausing a coroutine to let another operation finish using await.
import asyncio
from time import ctime

async def main():
    print(f"{ctime()} ->Task started.")

    await asyncio.sleep(1)  # Simulate a long-running operation


    print(f"{ctime()} -> Main Task finished.")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop    