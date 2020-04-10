import sqlite3

db = '../../introduction_dir/test.db'


def create_table():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    r = cursor.execute('CREATE TABLE IF NOT EXISTS user (id INT  , name VARCHAR(20))')
    print('create table-->', r)


def insert():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    r = cursor.execute('INSERT INTO user (id, name) VALUES (1, \'Michael\')')
    r = cursor.execute('INSERT INTO user (id, name) VALUES (2, \'Rose\')')
    r = cursor.execute('INSERT INTO user (id, name) VALUES (3, \'Iverson\')')
    print('insert-->', r)
    print('rowcount-->', cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()


def select():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    r = cursor.execute('SELECT * FROM user WHERE id>?', (1,))
    values = cursor.fetchall()
    print('values-->', values)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_table()
    insert()
    select()
