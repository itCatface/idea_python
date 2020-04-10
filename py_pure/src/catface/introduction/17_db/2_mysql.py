import mysql.connector

# 连接
conn = mysql.connector.connect(user='root', password='root', database='mybatis')
cursor = conn.cursor()

# 建表
# cursor.execute('CREATE TABLE IF NOT EXISTS py_user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')

# 插入[执行insert等操作后需要调用commit()提交事物]
# for i in range(10):
#     id, name = 'id:' + str(i), 'name:catface-' + str(i)
#     cursor.execute('INSERT INTO py_user (id, name) VALUES (%s, %s)', [id, name])
# cursor.rowcount
# conn.commit()
# conn.close

# 查询
cursor.execute('SELECT * from py_user WHERE id = %s', ('id:7',))
value = cursor.fetchall()
cursor.close()
conn.close
print('value-->', value)
