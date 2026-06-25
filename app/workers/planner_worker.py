import time

from app.queue.memory_queue import planner_queue


def start():

    print("Planner Worker Started")

    while True:

        job = planner_queue.get()

        print()

        print("========== WORKER ==========")

        print(f"Analisa : {job['name']}")

        print(f"Platform : {job['platform']}")

        print("============================")

        time.sleep(3)

        planner_queue.task_done()
