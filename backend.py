#This is the backend for signup page, which is the table for buyer and seller
#
#Insertion id increment

import sqlite3

def createUser(usertype):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    if usertype==False:
        cur.execute("""create table if not exists Buyer
        (id integer primary key,
        firstname text,
        lastname text,
        username text,
        password text,
        email text,
        phone text,
        address text,
        creditcard text);
        """)
    else:
        cur.execute("""create table if not exists Seller
        (id integer primary key,
        firstname text,
        lastname text,
        username text,
        password text,
        email text,
        phone text,
        address text,
        creditcard text);
        """)
    conn.commit()
    conn.close()



def createDevice():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("""create table if not exists
    Device (id integer primary key,
     developer text,
     name text,
     model text,
     year text,
     condition text);""")
    conn.commit()
    conn.close()



def createOffer():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("""create table if not exists Offer
    (device_id integer,
    seller_id integer,
     status text,
     date text,
     price real,
     foreign key(device_id) references Device(id),
     foreign key(seller_id) references Seller(id));""")
    conn.commit()
    conn.close()






def createWish():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("""create table if not exists
    Wish(device_id integer,
    buyer_id integer,
    creation_date text,
     foreign key(device_id) references Device(id),
     foreign key(buyer_id) references Buyer(id));""")
    conn.commit()
    conn.close()




def createShipment():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute(
    """create table if not exists Shipment(
    device_id integer,
    buyer_id integer, 
    seller_id integer,
    tracking_number text unique,
    carrier text,
    expected_arrival_date text,
    shipping_address text,
    foreign key(device_id) references Device(id),
     foreign key(buyer_id) references Buyer(id),
     foreign key(seller_id) references Seller(id)
    )""")
    conn.commit()
    conn.close()




def createDeviceTransaction():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("""
    create table if not exists DeviceTransaction
    (
    buyer_id integer,
    seller_id integer,
	seller_bank_account text,
    buyer_creditcard text,
	device_id integer,
    transaction_date  text,
    foreign key(device_id) references Device(id),
    foreign key(buyer_id) references Buyer(id),
    foreign key(seller_id) references Seller(id)
    )
    """)
    conn.commit()
    conn.close()

def insertBuyer(firstname,lastname,username,password,email,phone,address,creditcard):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("SELECT id FROM Buyer ORDER BY id DESC LIMIT 1;")
    id = 1
    result = cur.fetchone()
    if result != None:
        id = result[0] + 1
    cur.execute("""insert into Buyer
    values(?,?,?,?,?,?,?,?,?)""",(id,firstname,lastname,username,password,email,phone,address,creditcard))
    conn.commit()
    conn.close()


def insertSeller(firstname,lastname,username,password,email,phone,address,creditcard):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("SELECT id FROM Seller ORDER BY id DESC LIMIT 1;")
    id = 1
    result = cur.fetchone()
    if result != None:
        id = result[0] + 1
    cur.execute("""insert into Seller
    values(?,?,?,?,?,?,?,?,?);""",(id,firstname,lastname,username,password,email,phone,address,creditcard))
    conn.commit()
    conn.close()




def insertDevice(developer,name,model,year,condition):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("SELECT id FROM Device ORDER BY id DESC LIMIT 1;")
    id = 1
    result = cur.fetchone()
    if result != None:
        id = result[0] + 1
    cur.execute("""insert into Device
    values(?,?,?,?,?,?) ;""",(id,developer,name,model,year,condition))
    conn.commit()
    conn.close()


def insertOffer(device_id,seller_id,status,date,price):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    # cur.execute("SELECT id FROM Offer ORDER BY id DESC LIMIT 1;")
    # id=cur.fetchone()[0]
    # id+=1
    cur.execute("""insert into Offer
    values(?,?,?,?,?);""",(device_id,seller_id,status,date,price))
    conn.commit()
    conn.close()


def insertDeviceTransaction(buyer_id,seller_id,seller_creditcard,buyer_creditcard,device_id,transaction_date):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    # cur.execute("SELECT id FROM DeviceTransaction ORDER BY id DESC LIMIT 1;")
    # id=cur.fetchone()[0]
    # id+=1
    cur.execute("""insert into DeviceTransaction
    values(?,?,?,?,?,?);""",(buyer_id,seller_id,seller_creditcard,buyer_creditcard,device_id,transaction_date))
    conn.commit()
    conn.close()


def insertWish(device_id,buyer_id,creation_date):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    # id=cur.execute("SELECT id FROM Wish ORDER BY id DESC LIMIT 1;")
    # id+=1
    cur.execute("SELECT * FROM Wish where device_id = ? AND buyer_id = ?;", (device_id, buyer_id))
    result = cur.fetchone()
    if result:
        print ("Cannot add to wishlist, item already in wishlist")
        conn.close()
        return None

    cur.execute("""insert into Wish
    values(?,?,?);""",(device_id,buyer_id,creation_date))
    conn.commit()
    conn.close()


def insertShipment(device_id,buyer_id,seller_id,tracking_number,carrier,expected_arrival_date,shipping_address):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    # cur.execute("SELECT id FROM Shipment ORDER BY id DESC LIMIT 1;")
    # id=cur.fetchone()[0]
    # id+=1
    cur.execute("""insert into Shipment
    values(?,?,?,?,?,?,?);""",(device_id,buyer_id,seller_id,tracking_number,carrier,expected_arrival_date,shipping_address))
    conn.commit()
    conn.close()


def deleteOffer(device_id):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("delete from Offer where device_id=?;",(device_id,))
    conn.commit()
    conn.close()






def deleteDevice(device_id):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("delete from Device where id=?;",(device_id,))
    conn.commit()
    conn.close()



def deleteWish(device_id):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("delete from Wish where device_id=?;",(device_id,))
    conn.commit()
    conn.close()

def updateSeller(id,firstname,lastname,username,password,email,phone,address,creditcard):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("update products set firstname=?,lastname=?,username=?,password=?,email=?,phone=?,address=?,creditcard=? where id=?",(firstname,lastname,username,password,email,phone,address,creditcard,id))
    conn.commit()
    conn.close()


def updateBuyer(id,firstname,lastname,username,password,email,phone,address,creditcard):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("update Buyer set firstname=?,lastname=?,username=?,password=?,email=?,phone=?,address=?,creditcard=? where id=?",(firstname,lastname,username,password,email,phone,address,creditcard,id))
    conn.commit()
    conn.close()


def updateOffer(device_id,price):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("update Offer set price=? where device_id=?",(price,device_id))
    conn.commit()
    conn.close()




def updateDevice(id,developer,name,model,year,condition):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("update Device set developer=?,name=?,model=?,year=?,condition=? where id=?",(developer,name,model,year,condition,id))
    conn.commit()
    conn.close()


def getBuyerIDbyUsername(username):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("select id from buyer where username = ?",(username,))
    result = cur.fetchone()
    conn.commit()
    conn.close()
    if result:
        return int(result[0])
    return None


def getSellerIDbyUsername(username):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("select id from seller where username = ?",(username,))
    result = cur.fetchone()
    conn.commit()
    conn.close()
    if result:
        return int(result[0])
    return None

def dropBuyer():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("drop table if exists buyer")
    result = cur.fetchone()
    conn.commit()
    conn.close()

def dropSeller():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("drop table if exists seller")
    result = cur.fetchone()
    conn.commit()
    conn.close()

def dropDevice():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("drop table if exists Device")
    result = cur.fetchone()
    conn.commit()
    conn.close()

def dropOffer():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("drop table if exists Offer")
    result = cur.fetchone()
    conn.commit()
    conn.close()

def dropWish():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("drop table if exists Wish")
    result = cur.fetchone()
    conn.commit()
    conn.close()

def dropShipment():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("drop table if exists Shipment")
    result = cur.fetchone()
    conn.commit()
    conn.close()

def dropDevicetransaction():
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("drop table if exists Devicetransaction")
    result = cur.fetchone()
    conn.commit()
    conn.close()

# return True if username exists
def checkUsernameExist(username):
    ret = False
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("select * from Buyer where username = ?", (username,))
    result = cur.fetchone()
    if result:
        ret = True
    cur.execute("select * from Seller where username = ?", (username,))
    result = cur.fetchone()
    if result:
        ret = True
    conn.commit()
    conn.close()
    return ret

def selectDeviceIdByOther(developer,name,model,year,condition):
    conn=sqlite3.connect("secondhand.sqlite3")
    cur=conn.cursor()
    cur.execute("select id from  Device where developer = ? and name=? and model=? and year=? and condition=?", (developer,name,model,year,condition))
    device_id=cur.fetchone()[0]
    conn.commit()
    conn.close()
    return device_id


def database_intiation():
    # dropBuyer()
    # dropSeller()
    # dropDevice()
    # dropOffer()
    # dropWish()
    # dropShipment()
    # dropDevicetransaction()

    createUser(True)
    createUser(False)
    createDevice()
    createOffer()
    createWish()
    # createShipment()
    createDeviceTransaction()


database_intiation()
