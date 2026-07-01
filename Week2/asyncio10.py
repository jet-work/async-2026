# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio

async def calculate_bill(customer, base_price):
    await asyncio.sleep(1)  # Simulate a long-running operation
    final_price = base_price * 1.07  # Add 7% tax
    return final_price 

async def main():
    # Create tasks for calculating bills for two customers
    task_a = asyncio.create_task(calculate_bill("Alice", 100))
    task_b = asyncio.create_task(calculate_bill("Bob", 200))

    # Wait for both tasks to complete and get their results
    bill_a = await task_a
    bill_b = await task_b

    print(f"Final bill for Alice: ${bill_a:.2f}")
    print(f"Final bill for Bob: ${bill_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine using the event loop   
     