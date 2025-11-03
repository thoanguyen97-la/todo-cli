import task_utils
from task_utils import add_task
PASSED=0
FAILED=0
def assert_equal(actual,expected,message=""):
    global PASSED,FAILED
    try:
        assert actual==expected,f"Expected {expected} but got {actual}"
        print("✅ PASSED")
        PASSED += 1
    except AssertionError as e:
        print(f"❌ FAILED - {e}.{message}")
        FAILED+=1
def run_fr01_tests():
    print("---run FR01 tests---")
    # TC01: Thêm task hợp lệ -> return True, list tăng 1 phần tử, tên được strip
    print("TC01: Thêm task hợp lệ")
    tasks=[]
    result= add_task(tasks,"học python")
    assert_equal(result,True,"Add task thành công")
    assert_equal(len(tasks),1,"Chỉ add 1 task")
    assert_equal(tasks[0]["name"],"học python","Tên task được strip")
    # TC02: Thêm task rỗng
    print("TC02: Thêm task rỗng")
    tasks = [{"name": "Học python"}]
    result = add_task(tasks, "")
    assert_equal(result, False, "name rỗng không add vào")
    assert_equal(len(tasks), 1, "không thêm task mới")

    # TC03: Thêm task chỉ có khoảng trắng -> return False, list không đổi
    print("# TC03: Thêm task chỉ có khoảng trắng")
    tasks = [{"name": "Học python"}]
    result = add_task(tasks, "      ")
    assert_equal(result,False,"name sau khi strip rỗng không add vào")
    assert_equal(len(tasks),1,"không thêm task mới")

    #TC04: name có space 2 đầu -> True và lưu tên đã strip
    print("# TC04: name có space 2 đầu")
    tasks = []
    result = add_task(tasks, "   học python   ")
    assert_equal(result, True, "trả về true khi add thành công")
    assert_equal(len(tasks), 1, "chỉ add 1 task")
    assert_equal(tasks[0]["name"],"học python","tên task phải được strip")

    #TC05: name nhỏ hơn 3 ký tự
    print("# TC05: name có 2 ký tự")
    tasks = []
    try:
        result = add_task(tasks, "ab")
        print(f"❌ FAILED - Không raise ValueError khi name < 3 ký tự")
    except ValueError as e:
        assert_equal(str(e),"tên task phải có ít nhất 3 ký tự","Message lỗi đúng")

    #TC06: add task name đã tồn tại
    print("TC06: add task name đã tồn tại")
    task=[{"name": "Học python"}]
    result= add_task(task, "học python")
    assert_equal(result,False,"không add name đã tồn tại")
    assert_equal(len(tasks),1,"không thêm mới task")

if __name__ == "__main__":
    try:
        run_fr01_tests()
    except Exception as e:
        print("có lỗi ngoài dự kiến, không thể chạy test")
    finally:
        print("All test cases are executed!")
        print(f"RESULT: PASSED: {PASSED}, FAILED: {FAILED}")







