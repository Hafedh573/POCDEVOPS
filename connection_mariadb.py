'''
import mysql.connector
#*36342DF49762A4AC4BE08FBD3207679E1D6A16E7
#An0thrS3crt
mydb=mysql.connector.connect(host="127.0.0.1",user="citizix_user",passwd="An0thrS3crt")
print(mydb)
if (mydb):
  print("Connection to Mariadb established successfully")
else:
  print("Connection to Mariadb failed")
mycursor=mydb.cursor()
#mycursor.execute("create database test_bd")
mycursor.execute("show databases")
for db in mycursor:
  print(db)
'''
print('Good morning')
