import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='class',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

cursor.execute('create database if not exists student_db')

cursor.execute('use student_db')

cursor.execute('create table if not exists student_manager('
'id int auto_increment primary key, '
'name varchar(50) not null, '
'age int default 18, '
'score int);')

def add_student(name, score, age):
    sql = f'insert into student_manager(name, score, age) values("{name}", {score}, {age})'
    cursor.execute(sql)
    connection.commit()
    print("添加学生成功")


def get_student():
    sql = f'select * from student_manager;'
    cursor.execute(sql)
    return cursor.fetchall()

def change_student(id, name, score, age):
    sql = f'update student_manager set name="{name}", score = {score}, age = {age} where id = {id};'
    cursor.execute(sql)
    connection.commit()
    print("修改学生成功")

def delete_student(id):
    sql = f'delete from student_manager where id = {id};'
    cursor.execute(sql)
    connection.commit()
    print("删除学生成功")

def order_by_score_desc():
    sql = f'select * from student_manager order by score desc;'
    cursor.execute(sql)
    return cursor.fetchall()

def get_all_id():
    sql = f'select id from student_manager;'
    cursor.execute(sql)
    return [item['id'] for item in cursor.fetchall()]


