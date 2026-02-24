import pymysql

connection=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='class',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = connection.cursor()
sql ="select * from sanguo;"
cursor.execute(sql)
result = cursor.fetchall()
for itme in result:
    print(itme)

sql ="insert into sanguo(name ,sex,country,attack,defense) values ('孔明','男','蜀',256,63);"
cursor.execute(sql)
connection.commit()

sql ="select * from sanguo;"
cursor.execute(sql)
result = cursor.fetchall()
for itme in result:
    print(itme)

sql ="update sanguo set name='诸葛' where name ='诸葛亮';"
cursor.execute(sql)
connection.commit()



sql ="delete from sanguo  where name ='诸葛';"
cursor.execute(sql)
connection.commit()

sql ="select * from sanguo;"
cursor.execute(sql)
result = cursor.fetchall()
for itme in result:

    print(itme)
