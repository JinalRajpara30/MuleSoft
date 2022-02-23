import sqlite3
class demo:
    #create database
    
    #make constructor for create table
    def __init__(self):
        self.con=sqlite3.connect("movie.db")
        #self.con.execute("create table movies(movie_name text,lead_act text,actress text,year_rel int,dir_nm text)")
        #self.con.commit()
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
ds.insert()
ds.delete()
ds.disp()
