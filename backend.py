import sqlite3

def connect():
    conn=sqlite3.connect("products.db")
    cur=conn.cursor()
    cur.execute("create table if not exists products (id integer primary key,product text, price real, year integer, name text, phone text, email text, address text)")
    conn.commit()
    conn.close()


def insert(product,price,year,name,phone,email,address):
    conn=sqlite3.connect("products")
    cur=conn.cursor()
    cur.execute("insert into products values (NULL,?,?,?,?,?,?,?)",(product,price,year,name,phone,email,address))
    conn.commit()
    conn.close()
    view()


def view():
    
