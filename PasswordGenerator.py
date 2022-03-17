import random
import sys
import pymysql

class passwordGeneratorClass :
    
        
    def database_controller (self, query):
        
        conn = pymysql.connect( 
            host='localhost', 
            user='root',  
            password = "root", 
            db='stored_passwords', 
            ) 
        cur = conn.cursor() 
        try:
             cur.execute(query) 
             conn.commit() 
        except:
             conn.rollback()
        output = cur.fetchall() 
        conn.close() 
        return output
        
  
      

        
        
    def __password_generator(self):
        low_cases = "abcdefghiklmnopqrstuvwxyz"
        upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "123456789"
        passwd = ""
        for _ in range(0,4):
            passwd = passwd + random.choice(low_cases) + random.choice(upper_cases) + random.choice(numbers )
        return passwd


    def __password_reader(self, required_password):
        query = "SELECT password FROM  stored_passwords.passwords WHERE Appsname = \"" + required_password    + "\" " 
        response = self.database_controller(query)
        return response 


    def __password_writter(self, required_password):
        new_password = self.__password_generator()
        query = "INSERT INTO stored_passwords.passwords (AppsName, password) VALUES (\"" +required_password + "\", \"" + new_password + "\");"
        response = self.database_controller(query)
        print("the password for " + required_password + " will be " + new_password + " and it has been sotred correctly in the local DATABASE ")


    def __password_cheker(self, name_of_app):
        if self.__password_reader(name_of_app):
            print("the password for the "+ name_of_app + " app is the following one: ")
            print ( self.__password_reader(name_of_app) )
        else:
            self.__password_writter(name_of_app)

    def app_starter(self):
        if (len(sys.argv) == 3 and sys.argv[1].lower() == "app".lower()):
            self.__password_cheker(sys.argv[2])
        else:
            name_of_app = input("please type the name of the app ")
            self.__password_cheker(name_of_app)

paswordGeneratorApp = passwordGeneratorClass()
paswordGeneratorApp.app_starter()

