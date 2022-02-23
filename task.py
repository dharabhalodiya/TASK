import sqlite3  
#database create
conn = sqlite3.connect('movies.db')  
print("database conected") 

#table created
conn.execute('''''CREATE TABLE moviess
       (NAME TEXT NOT NULL,
       ACTOR TEXT NOT NULL,
       ACTRESS TEXT NOT NULL,
       DIRECTOR TEXT NOT NULL,
       YEAR OF RELEASE INT NOT NULL);''')  
print ("Table created successfully") 

#record insertted
conn.execute("INSERT INTO moviess (NAME ,ACTOR,ACTRESS,DIRECTOR,YEAR OF RELEASE) VALUES ('sivangi','rahul','mona','aehmad',2019)")
conn.execute("INSERT INTO moviess (NAME ,ACTOR,ACTRESS,DIRECTOR,YEAR OF RELEASE) VALUES ('rena','kapil','priya','aehmad',2020)")

#select record
data = conn.execute("select * from moviess")

for row in data:  
   print ("NAME = ", row[0])  
   print ("ACTOR = ", row[1]) 
   print ("ACTRESS = ", row[2])  
   print ("DIRECTOR = ", row[3])
   print ("YEAR OF RELEASE = ", row[4])  
  
conn.close();    