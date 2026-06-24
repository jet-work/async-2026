from time import sleep, ctime, time, process_time
import os
import threading
import psutil

# ฟังก์ชันจำลองการชงกาแฟทีละแก้ว (Synchronous)
def make_coffee(customer_name):
    # หา PID และ Thread ID ของงาน
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"[{ctime()}] | PID: {pid} | TID: {thread_id} | Thread Name: {thread_name} | กำลังชงกาแฟให้ ลูกค้า {customer_name}...")

    # ใช้เวลาในการชง 5 วินาที
    sleep(5)

    print(f"[{ctime()}] | PID: {pid} | TID: {thread_id} | Thread Name: {thread_name} | ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    queue = ['A', 'B', 'C']

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"[{ctime()}] | Main PID: {main_pid} | Main TID: {main_tid} === เริ่มระบบร้านกาแฟแบบ Synchronous ===")

    start_time = time()
    start_cpu = process_time()

    # ชงกาแฟตามลำดับคิว (ทีละคน)
    for customer in queue:
        make_coffee(customer)

    duration = time() - start_time
    cpu_duration = process_time() - start_cpu

    # ใช้ psutil เพื่อวัดการใช้ RAM
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    print("\n[ข้อมูล Synchronous]")
    print(f"เวลาที่ใช้จริง (Wall Time): {duration:.2f} วินาที")
    print(f"เวลา CPU ที่ใช้จริง (CPU Time): {cpu_duration:.4f} วินาที")
    print(f"หน่วยความจำ Memory (RAM) ที่ใช้: {mem_mb:.2f} MB")

if __name__ == "__main__":
    main()