import mysql.connector as ms
cn=ms.connect(host='localhost',user='root',password = '')
cr=cn.cursor()
cr.execute("Show databases")
x = []
for i in cr:
    x.append(i)
    print(i,sep = ')')
db = input("Enter name of database: ")
for i in x:
    print(i)
if db in cr:
    print("exists")
cn.close()