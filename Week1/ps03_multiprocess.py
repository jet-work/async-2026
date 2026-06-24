from time import sleep, ctime, time, process_time
import multiprocessing
import threading
import os
import psutil

# ฟังก์ชันของการทำงานพนักงานทำกาแฟทีละ 1 คน
def make_coffee(customer_name, result_queue):

    # หา PID ของหน่วยประมวลผลนี้ (ซึ่งจะแยกกันในแต่ละ Process)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"[{ctime()}] | PID: {pid} | TID: {thread_id} | Thread Name: {thread_name} | กำลังชงกาแฟให้ ลูกค้า {customer_name}...")

    start_cpu = process_time()

    # จำลองงานคำนวณ (CPU-bound) เล็กน้อย และรอ 5 วินาที
    sum(i * i for i in range(1000000))
    sleep(5)

    cpu_duration = process_time() - start_cpu

    print(f"[{ctime()}] | PID: {pid} | TID: {thread_id} | Thread Name: {thread_name} | ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

    # ส่งค่าการใช้ RAM และ CPU ของตัวเองกลับไปที่ Main Process
    process = psutil.Process(pid)
    mem_mb = process.memory_info().rss / (1024 * 1024)

    result_queue.put((mem_mb, cpu_duration))