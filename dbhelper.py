import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                                   port='3306',
                                   user='root',
                                   password='sqlpaul',
                                   database='world')
        query= 'create table if not exists user(userID int primary key, userName varchar(200), phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print('Created')

    #Insert data
    def insert_user(self,userid,username,phone):
        query="insert into user(userID,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('This Patient added to Database')

    #Fech all
    def fech_all(self):
        query=' select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        for i in cur:
            print('UserID: ',i[0])
            print('UserName: ',i[1])
            print('Phone: ',i[2])
            print()
            print()

    #Delete all
    def delete_all(self,userid):
        query=' delete from user where userID={}'.format(userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit() # it will permanently delete the data
        print('This Patient remove from Database')

    #update
    def update_user(self,userID,newName,newPhone):
        query="update user set userName='{}', phone='{}' where userID={}".format(newName,newPhone,userID)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Updated')