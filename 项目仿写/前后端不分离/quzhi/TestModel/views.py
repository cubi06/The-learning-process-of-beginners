from collections import defaultdict
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.utils import timezone
import json
from django.http import JsonResponse
# Create your views here.

def login_required(view_func):
    def wrapper(request,*args, **kwargs):
        user_id=request.session.get("userid")
        if not user_id:
            return render(request,"index.html",{"error":"请先登录",})
        try:
            UserInfo.objects.get(id=user_id)
            return view_func(request, *args, **kwargs)
        except Exception as e:
            rquest.session.flush()
            return render(request,"index.html",{"error":"登录信息已失效，请重新登录",})
    return wrapper



@login_required
def visual_home(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    today=timezone.now().date()
    today_check,created=DateCheckInfo.objects.get_or_create(date=today)
    all_completed_task_id=[item[0] for item in today_check.task_done.values_list('id')]
    user_task_id=[item[0] for item in obj.tasks.values_list('id')]
    completed_task_ids=list(set(all_completed_task_id)&set(user_task_id))
    total_tasks =obj.tasks.count()
    completed_task_today=len(completed_task_ids)
    all_todos=obj.todos.all()
    total_todos=all_todos.count()
    undo=obj.todos.filter(state=0)
    completed_todos=obj.todos.filter(state=1).count()
    return render(request,"home.html",{
        "user":obj,
        "completed_task_ids":completed_task_ids,
        "total_tasks":total_tasks,
        "completed_task_today":completed_task_today,
        "all_todos":all_todos,
        "total_todos":total_todos,
        "undo":undo,
        "completed_todos":completed_todos
    })

def visual_login(request):
        return render(request,"index.html")

def visual_register(request):
    name=request.POST.get("name")
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")
    if not name or not password or not confirm_password:
        return render(request,"index.html",{
            "error":"请填写完整信息",
            "show_register":True
        })
    if password!=confirm_password:
        return render(request,"index.html",{
            "error":"两次密码不一致",
            "show_register": True
        })
    if UserInfo.objects.filter(name=name).exists():
        return render(request, "index.html", {
            "error": "这个用户名被注册，请选择别的用户名",
            "show_register": True
        })
    obj=UserInfo.objects.create(
        name=name.strip(),
        password=password.strip(),
        task_finish_number=0,
        todo_finish_number=0
    )
    request.session["userid"] = obj.id
    return redirect("/home/")

def login_form(request):
    if request.method == "POST":
        username = request.POST.get("account")
        password = request.POST.get("password")
        if not username or not password:
            return render(request, "index.html", {
                "error": "请输入用户密码"
            })
        try:
            obj=UserInfo.objects.get(name=username,password=password)
            request.session["userid"] = obj.id
            return redirect("/home/")
        except Exception as e:
            return render(request, "index.html", {
                "error": "用户名或密码错误",
                "show_register": True
            })
    return render(request,"index.html")

@login_required
def newtasks(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    if request.method=="POST":
        name = request.POST.get("name")
        begin = request.POST.get("begin")
        end = request.POST.get("end")
        obj.tasks.create(name=name,begin=begin,end=end)
        return redirect("/home/")
    return redirect("/home/")

@login_required
def newtodos(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    if request.method=="POST":
        name = request.POST.get("name")
        date = request.POST.get("date")
        obj.todos.create(name=name,date=date,state=0)
        return redirect("/home/")
    return redirect("/home/")

@login_required
def task_complete(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    data = json.loads(request.body)

    todoid=data.get("todo_id")
    if todoid==0:
        task_id = data.get("task_id",0)
        task=TaskInfo.objects.get(id=task_id)
        date=timezone.now().date()
        today_check,created=DateCheckInfo.objects.get_or_create(date=date)
        if task in today_check.task_done.all():
            return JsonResponse({"error":"任务已经完成"})
        today_check.task_done.add(task)
        obj.task_finish_number+=1
        obj.save()

        return JsonResponse({"success":True,"message":"操作成功"}),redirect("/home/")


    taskid=data.get("task_id")
    if taskid==0:
        todo_id = data.get("todo_id")
        todo=TodoInfo.objects.get(id=todo_id)
        if todo.state==1:
            return JsonResponse({"error":"任务已经完成"})
        todo.state=1
        obj.todo_finish_number+=1
        todo.save()
        return JsonResponse({"success":True,"message":"操作成功"}),redirect("/home/")

@login_required
def infochange(request):
    password=request.POST.get("password")
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    obj.password= password
    obj.save()
    return redirect("/home/")

@login_required
def logout(request):
    if 'userid' in request.session:
        request.session.flush()
    return render(request,"index.html",{
        "success":"注销成功",
    })

@login_required
def visualization(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    date=timezone.now().date()
    today_check,created=DateCheckInfo.objects.get_or_create(date=date)
    completed_task_ids= today_check.task_done.values_list('id',flat=True)
    total_tasks =obj.tasks.count()
    completed_tasks_today=len(completed_task_ids)
    pending_task = total_tasks-completed_tasks_today

    return render(request,"page.html",{
        'user':obj,
        'completed_task_ids':completed_task_ids,
        'total_tasks':total_tasks,
        'completed_tasks_today':completed_tasks_today,
        'pending_task':pending_task
    })

@login_required
def delete_task(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    data=json.loads(request.body)
    task_id =data.get("task_id")
    odj_tasks=obj.tasks.all()
    try:
        task=TaskInfo.objects.get(id=task_id)
    except Exception as e:
        return JsonResponse({"error":"任务不存在"})
    if task not in odj_tasks:
        return JsonResponse({"error":"此数据不是用户数据"})
    date=timezone.now().date()
    today_check,created=DateCheckInfo.objects.get_or_create(date=date)
    today_check.task_done.remove(task)
    if obj.task_finish_number>0:
        obj.task_finish_number-=1
        obj.save()
    obj.tasks.remove(task)
    task.delete()
    return JsonResponse({"success":True,"message":"删除成功"})

@login_required
def visual_todo_lists(request):
    obj_id = request.session.get("userid")
    obj = UserInfo.objects.get(id=obj_id)
    total_todos=obj.todos.count()
    completed_todos=obj.todos.filter(state=1).count()
    pending_todos=obj.todos.filter(state=0).count()

    return render(request,"todo.html",{
        'user':obj,
        'total_todos':total_todos,
        'completed_todos':completed_todos,
        'pending_todos':pending_todos
    })

@login_required
def delete_todo(request):
    if request.method!="POST":
        return JsonResponse({"error":"请求方式错误",'success': False})
    data=json.loads(request.body)
    todo_id =data.get("todo_id")
    try:
        todo=TodoInfo.objects.get(id=todo_id)
    except Exception as e:
        return JsonResponse({"error":"待办事项不存在",'success': False})
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    if todo not in obj.todos.all():
        return JsonResponse({"error":"此数据不是用户数据",'success': False})
    if obj.todo_finish_number>0:
        obj.todo_finish_number-=1
        obj.save()
    obj.todos.remove(todo)
    todo.delete()
    return JsonResponse({"success":True,"message":"删除成功"})

@login_required
def visual_displaytree(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    return render(request,"displaytree.html",{
        'user':obj,
    })

@login_required
def visual_pinechart(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    todo_count=obj.todos.filter(state=0).count()
    done_count=obj.todos.filter(state=1).count()

    from datetime import timedelta
    daily_stats = []
    today = timezone.now().date()
    for i in range(6, -1, -1):
        try:
            date_check =today - timedelta(days=i)
            completed_task_ids=DateCheckInfo.objects.get(date=date_check).task_done.values_list('id',flat=True)
            user_task_ids=obj.tasks.values_list('id',flat=True)
            completed_tasks=len(set(completed_task_ids) & set(user_task_ids))
        except Exception as e:
            completed_tasks=0
        daily_stats.append({
            'date':date_check.strftime("%m/%d"),
            "completed":completed_tasks,
        })
    return render(request,"pinechart.html",{
        'user':obj,
        'done':done_count,
        'todo':todo_count,
        'daily_stats':daily_stats
    })

@login_required
def npc_choice(request,id):
    character_name=["Feilen","Frieren","Himmel","Stark"]
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    chat_history=ChatMessage.objects.filter(user=obj,npc_id=id).order_by('timestamp')
    request.session['npc_id']=id
    return render(request,"npc.html",{
        'user':obj,
        'npc_id':id,
        'npc_name':character_name[id],
        'chat_history':chat_history
    })

from openai import OpenAI

client=OpenAI(
    api_key="******",
    base_url="https://api.moonshot.cn/v1",
)
history = []
def chat(query):
    history.append({
        "role": "user",
        "content": query,
    })
    completion=client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=history,
    )
    res = completion.choices[0].message.content
    if len(history) > 7:
        history.pop(0)
    history.append({
        "role": "assistant",
        "content": res,
    })
    return res

@login_required
def npc_dialog(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    npc_id=request.session.get("npc_id")
    character_name=["Feilen","Frieren","Himmel","Stark"]
    npc_name=character_name[npc_id]

    message=request.POST.get("text")
    if message:
        ChatMessage.objects.create(
            user=obj,
            npc_id=npc_id,
            npc_name=npc_name,
            message_type="user",
            content=message,
        )
        try:
            reply=chat(message)
        except Exception as e:
            reply=f"抱歉，{npc_name}暂时无法回答问题，请稍后再试。"
        ChatMessage.objects.create(
            user=obj,
            npc_id=npc_id,
            npc_name=npc_name,
            message_type="npc",
            content=reply,
        )
    return redirect(f"/npcchoice/{npc_id}/")

@login_required
def clear_chat(request):
    obj_id=request.session.get("userid")
    obj=UserInfo.objects.get(id=obj_id)
    npc_id=request.session.get("npc_id")
    ChatMessage.objects.filter(user=obj,npc_id=npc_id).delete()
    return JsonResponse({'success': True,'message': "清除成功"})