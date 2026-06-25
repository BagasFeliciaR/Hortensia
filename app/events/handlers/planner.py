from app.queue.memory_queue import planner_queue


def on_program_created(data):

    planner_queue.put(data)

    print()

    print("========== PLANNER ==========")

    print("Masuk Queue")

    print(f"Queue Size : {planner_queue.qsize()}")

    print("=============================")

    print()
