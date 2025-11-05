import json

FILE_PATH = "tasks.json"

def add_task(tasks: list[dict[str,str]],name: str):
    """
        Thêm một task mới vào danh sách.
        - Yêu cầu: name không được rỗng sau khi strip(), tối thiểu 3 ký tự, không được trùng task
        - Trả về: True nếu thêm thành công, False nếu thất bại.
        """
    name=name.strip()
    if not name:
        return False
    if len(name) < 3:
        raise ValueError("tên task phải có ít nhất 3 ký tự")
    for task in tasks:
        if task["name"].lower() == name.lower():
            return False
    tasks.append({"name":name,"status":"To do"})
    save_tasks(tasks)
    return True

def show_task(tasks: list[dict[str,str]]):
    """Show danh sách các task
    -Yêu cầu: Hiển thị danh sách các task
    -Trả về: Danh sách task đang có, show message nếu danh sách rỗng"""
    if not tasks:
        message="Chưa có task nào!"
        print("Chưa có task nào!")
        return message
    lines=[]
    for i, task in enumerate(tasks,start=1):
        line=f"{i}. {task['name']} - {task['status']}"
        print(line)
        lines.append(line)
    result="/n".join(lines)
    return result

def delete_task(tasks,index):
    """Xoá task được chỉ định
    """
    removed= tasks.pop(index - 1)
    print(f"xoá thành công task {removed["name"]}")
    print("List task còn lại:")
    show_task(tasks)

def save_tasks(tasks):
    """Save task vào file json"""
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def load_task():
    """Load task json"""
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []





