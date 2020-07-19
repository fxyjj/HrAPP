import pymysql

db = pymysql.connect("localhost","root","Xsl123456*","HrAPP")

cursor = db.cursor()

cursor.execute("select * from Employer")

data = cursor.fetchall()

print(data)
print(len(data))

