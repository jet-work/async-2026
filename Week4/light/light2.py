import asyncio
import httpx
from time import time

BASE_URL = "http://172.16.2.117:8088"
STUDENT_ID = "6710301022"


async def set_light(client, light_id):
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    response = await client.post(url, json={"status": "ON"})
    result = response.json()
    print(light_id, "->", result)
    return result


async def main():
    start = time()

    async with httpx.AsyncClient() as client:
        tasks = [
            set_light(client, light_id)
            for light_id in ["light_1", "light_2", "light_3", "light_4"]
        ]
        await asyncio.gather(*tasks)

    print(f"Total time: {time() - start:.2f}s")


asyncio.run(main())