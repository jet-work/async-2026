# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def greet():
    print("Hello from the Event Loop!")

if __name__ == "__main__":
    asyncio.greet()  # coroutine using the event loop  


    asyncio.run(coro_object)  # coroutine using the event loop  