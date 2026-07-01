from time import sleep, ctime, time
import threading

def greet_diners(customer):
    print(f"{ctime()} | Greeting for customer {customer} ...")
    sleep(1.0)
    print(f"{ctime()} | Greeting for customer {customer}...Done!")

def customer_private_workflow(customer):
    greet_diners(customer)
    print(f"{ctime()} | Taking order for customer {customer} ...")
    sleep(1.0)
    print(f"{ctime()} | Finished taking order for customer {customer}...Done!")

    print(f"{ctime()} | Cooking for customer {customer} ...")
    sleep(1.0)
    print(f"{ctime()} | Finished cooking for customer {customer}...Done!") 

    print(f"{ctime()} | Preparing mini bar for customer {customer} ...")
    sleep(1.0)
    print(f"{ctime()} | Finished preparing mini bar for customer {customer}...Done!")
    print(f"{ctime()} | Customer {customer} workflow completed.")

if __name__ == "__main__":
    customers = ["Alice", "Bob", "Charlie"]

    print(f"{ctime()} | === Multi-threading Restaurant Workflow ===")
    start_time = time()

    threads = []
    for customer in customers:
        t = threading.Thread(target=customer_private_workflow, args=(customer,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time() - start_time
    print(f"{ctime()} | Total time: {duration:.2f} seconds")
    print(f"{ctime()} | === Workflow completed ===")
