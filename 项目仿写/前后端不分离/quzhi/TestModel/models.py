from django.db import models

# Create your models here.
# 每日任务
class TaskInfo(models.Model):
    name = models.CharField(max_length=100)
    begin = models.DateField()
    end = models.DateField()
    frequency = models.IntegerField(default=1)

# 待办事项
class TodoInfo(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    state = models.IntegerField()

#用户表
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    task_finish_number = models.IntegerField(default=0)
    todo_finish_number = models.IntegerField(default=0)
    tasks = models.ManyToManyField(TaskInfo, related_name='tasks')
    todos = models.ManyToManyField(TodoInfo, related_name='todos')

# 每日任务检查表
class DateCheckInfo(models.Model):
    date =models.DateField()
    task_done =models.ManyToManyField(TaskInfo)

class ChatMessage(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    npc_id = models.IntegerField('NPC ID',default=0)
    npc_name = models.CharField('NPC Name',max_length=50,default='')
    message_type=models.CharField('Message Type',max_length=10,choices=[
        ('user','用户消息'),
        ('npc','NPC消息')
    ])
    content = models.TextField('消息内存')
    timestamp = models.DateTimeField('发送时间',auto_now_add=True)


