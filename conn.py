import sqlite3
class demo:
    #create database
    con=sqlite3.connect("movie.db")
    #make constructor for create table
    def __init__(self):
        # self.con.execute("create table movies(movie_name text,lead_act text,actress text,year_rel int,dir_nm text)")
        # self.con.commit()
    #make function for insert query
    def insert(self):
        self.con.execute("insert into movies(movie_name,lead_act,actress,year_rel,dir_nm)values('ready','salman','karina',2011,'abc')")
        self.con.commit()
    #make function for delete table
    def delete(self):
        self.con.execute("delete from movies")
        self.con.commit()
    #make function for fetch & select the data
    def disp(self):
       dt=self.con.execute("select movie_name,lead_act,actress,year_rel,dir_nm from movies")
        self.con.commit()
        for row in dt:
            print("movie_name:{}".formate(row[0]))
            print("lead_act:{}".formate(row[1]))
            print("actress:{}".formate(row[2]))
            print("year_rel:{}".formate(row[3]))
            print("dir_nm:{}".formate(row[4]))
#object of demo class & and calling the constructor & function 
ds=demo()
#choice 
while(True):
    print("1:insert data")
    print("2:Delete data")
    print("3:Display data")
    print("4:exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        ds.insert()
    elif choice==2:
        ds.delete()
    elif choice==3:
        ds.disp()
    elif choice==4:
        break
    else:
        print("enter valid choice")
