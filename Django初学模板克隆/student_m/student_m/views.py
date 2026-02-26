from django.shortcuts import render, HttpResponse
import json

def test_templates(request):
    # 产生一些数据
    data_dict = {
        "id": 1, "name": "张三", "age": 20,
        "grade": "计算机科学与技术1班", "score": 95,
        "sports": [1, 2, 3],
        "test_dict": {"a":"1", "b":"2"}
    }
    return render(request, "test_templates.html", data_dict)


def display_students(request):
    # 1. 读取json文件，渲染模版
    with open(r"", "r", encoding="utf-8") as f:
        # 加载json文件的方法 json.load()
        data = json.load(f)
    data_dict = {"students": data}
    print(data)
    return render(request, "display_students.html", data_dict)

def delete_students(request, stu_id):
    with open(r"", "r", encoding="utf-8") as f:
        # 加载json文件的方法 json.load()
        data = json.load(f)

    print("stu_id:", stu_id, type(stu_id))
    student_to_delete = None
    for student in data:
        print("student.id", student["id"], type(student["id"]))
        if student["id"] == stu_id:
            student_to_delete = student
            break

    print(student_to_delete)

    if student_to_delete:
        data.remove(student_to_delete)
        # 把删除后的data重写到json文件中
        with open(r"", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        data_dict = {"students": data}
        return render(request, "display_students.html", data_dict)
    return HttpResponse("删除失败，没有这个数据")

def add_students(request):
    if request.method == "GET":
        return render(request, "add_students.html")
    elif request.method == "POST":
        # 接受用户的数据
        name = request.POST.get("name")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        score = request.POST.get("score")
        if name and age and grade and score:
            with open(r"", "r", encoding="utf-8") as f:
                # 加载json文件的方法 json.load()
                data = json.load(f)

            if data:
                max_id = max([item["id"] for item in data])
                next_id = max_id + 1

            else:
                next_id = 1
            new_student = {
                "id": next_id,
                "name": name,
                "age": age,
                "grade": grade,
                "score": score,
            }
            data.append(new_student)
            with open(r"", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            # 写到json文件中
            # 返回添加成功
            return HttpResponse("添加成功")
        else:
            return HttpResponse("添加失败")
    else:
        return HttpResponse("不支持的请求方式")