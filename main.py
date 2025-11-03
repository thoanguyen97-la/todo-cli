from task_utils import add_task

if __name__ == "__main__":
    tasks=[]
    add_task(tasks,"learn code python")
    add_task(tasks,"learn english")
    add_task(tasks, "abc")
    add_task(tasks, "learn ENGLISH")
    for i,task in enumerate(tasks,start=1):
        print(f"{i}. {task['name']} - {task['status']}")
