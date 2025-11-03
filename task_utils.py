def add_task(tasks: list[dict[str,str]],name: str):
    """
        Thêm một task mới vào danh sách.
        - Yêu cầu: name không được rỗng sau khi strip().
        - Trả về: True nếu thêm thành công, False nếu thất bại.
        """
    name=name.strip()
    if not name:
        return False
    tasks.append({"name":name})
    return True