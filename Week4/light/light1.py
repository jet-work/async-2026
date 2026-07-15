import json
from urllib import request
from time import time

BASE_URL = "http://172.16.2.117:8088"
STUDENT_ID = "6710301022"

start = time()

for light_id in ["light_1", "light_2", "light_3", "light_4"]:
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    data = json.dumps({"status": "ON"}).encode()
    req = request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    
    with request.urlopen(req) as res:
        result = json.loads(res.read())
        print(light_id, "->", result)

print(f"Total time: {time() - start:.2f}s")