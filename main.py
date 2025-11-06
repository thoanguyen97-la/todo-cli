from task_utils import add_task, show_task, delete_task, load_task,save_tasks

if __name__ == "__main__":

    tasks=[]
    add_task(tasks,"learn code python")
    add_task(tasks,"learn english")
    add_task(tasks, "API Testing")
    show_task(load_task())
    while True:
        try:
            index= int(input("Nhập index cần xoá:"))
            if index <=0 or index > len(tasks):
                print("Index không hợp lệ!")
                continue
            else:
                delete_task(tasks,index)
                break
        except ValueError:
            print("Index không hợp lệ!")

