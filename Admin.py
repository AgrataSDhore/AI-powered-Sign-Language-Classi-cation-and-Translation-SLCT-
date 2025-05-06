import pymysql # type: ignore

conn=pymysql.connect(host="localhost",user="root",password="",db="contacts_db")

curr=conn.cursor()

def checkDBConnection():
    if(curr):
        return True
    else:
        return False
    
def addContactData(name,email,message):
    try:
        qry="INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
        data=(name,email,message)
        curr.execute(qry,data)
        conn.commit()
    except:
        print("An error has occured : Can not add the contact details !")
