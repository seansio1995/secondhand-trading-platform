import sqlite3

def connect():
    conn=sqlite3.connect("products.db")
    cur=conn.cursor()
    cur.execute("create table if not exists products (id integer primary key,product text, price real, year integer, name text, phone text, email text, address text)")
    conn.commit()
    conn.close()


def insert(product,price,year,name,phone,email,address):
    conn=sqlite3.connect("products.db")
    cur=conn.cursor()
    cur.execute("insert into products values (NULL,?,?,?,?,?,?,?)",(product,price,year,name,phone,email,address))
    conn.commit()
    conn.close()
    view()


def view():
    conn=sqlite3.connect("products.db")
    cur=conn.cursor()
    cur.execute("select * from products")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(product="",price=0,year=0,name="",phone="",email="",address=""):
    conn=sqlite3.connect("products.db")
    cur=conn.cursor()
    cur.execute("select * from products where product=? or price=? or year=? or name=? or phone=? or email=? or address=?",(product,price,year,name, phone, email, address))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("products.db")
    cur=conn.cursor()
    cur.execute("delete from where id=?",(id,))
    conn.commit()
    conn.close()



def update(id,product,price,year,name,phone,email,address):
    conn=sqlite3.connect("products.db")
    cur=conn.cursor()
    cur.execute("update products set product=?, price=?, year=?, name=?, phone=?,email=?, address=? where id=?",(product,price,year,name,phone,email,address,id))
    conn.commit()
    conn.close()
