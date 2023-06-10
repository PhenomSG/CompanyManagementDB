import mysql.connector as ms
cn=ms.connect(host='localhost',user='root',password = '')
cr=cn.cursor()
cr.execute("Show databases")
for i in cr:
    print(i)
cn.close()