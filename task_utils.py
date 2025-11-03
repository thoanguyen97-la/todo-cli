def add_task(tasks: list[dict[str,str]],name: str):
    """
        Thêm một task mới vào danh sách.
        - Yêu cầu: name không được rỗng sau khi strip(), tối thiểu 3 ký tự, không được trùng task
        - Trả về: True nếu thêm thành công, False nếu thất bại.
        """
    name=name.strip().capitalize()
    if not name:
        return False
    if len(name) < 3:
        return False
    for task in tasks:
        if task["name"].lower() == name.lower():
            return False
    tasks.append({"name":name,"status":"To do"})
    return True