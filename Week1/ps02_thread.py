from time import sleep, ctime, time, process_time
import threading
import os
import psutil

# ฟังก์ชันจำลองการชงกาแฟทีละ 1 แก้ว
def make_coffee(customer_name):
    # PID และข้อมูล Thread
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"[{ctime()}] | PID: {pid} | TID: {thread_id} | Thread Name: {thread_name} | กำลังชงกาแฟให้ ลูกค้า {customer_name}...")

    # จำลองเวลาชงกาแฟ 5 วินาที
    sleep(5)

    print(f"[{ctime()}] | PID: {pid} | TID: {thread_id} | Thread Name: {thread_name} | ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    queue = ['A', 'B', 'C']

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"[{ctime()}] | Main PID: {main_pid} | Main TID: {main_tid} === เริ่มระบบร้านกาแฟแบบ Multi-Thread ===")

    start_time = time()
    start_cpu = process_time()

    threads = []

    # สร้างและเริ่ม Thread
    for customer in queue:
        th = threading.Thread(
            target=make_coffee,
            args=(customer,),
            name=f"Thread-{customer}"
        )

        threads.append(th)
        th.start()

    # รอให้ทุก Thread ทำงานเสร็จ
    for t in threads:
        t.join()

    duration = time() - start_time
    cpu_duration = process_time() - start_cpu

    # ใช้ psutil วัดการใช้ RAM
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    print("\n[ข้อมูล Multi-Thread]")
    print(f"เวลาที่ใช้จริง (Wall Time): {duration:.2f} วินาที")
    print(f"เวลา CPU ใช้งานสะสมจริง (CPU Time): {cpu_duration:.4f} วินาที")
    print(f"หน่วยความจำ Memory (RAM) ที่ใช้: {mem_mb:.2f} MB")

if __name__ == "__main__":
    main()