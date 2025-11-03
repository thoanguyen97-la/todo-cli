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
    print(result)
    return result