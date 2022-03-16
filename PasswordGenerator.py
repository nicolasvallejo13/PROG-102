import random
import sys
class passwordGeneratorClass :
    
        
    def __password_generator(self):
        low_cases = "abcdefghiklmnopqrstuvwxyz"
        upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "123456789"
        passwd = ""
        for _ in range(0,4):
            passwd = passwd + random.choice(low_cases) + random.choice(upper_cases) + random.choice(numbers )
        return passwd


    def __password_reader(self, required_password):
        with open('stored_passwords.txt') as file:
        
            for line in file:
                if line.split()[0].lower() == required_password.lower():
                    print("the password for the " + required_password +" app is the following one: " + line.split()[1])
                    return True
        return False


    def __password_writter(self, required_password):
        with open('stored_passwords.txt' , "a") as file:
            file.write('\n')
            new_password = self.__password_generator()
            file.write(required_password + " " + new_password)
            print("the password for " + required_password + " will be " + new_password + " and it has been sotred correctly in the txt file ")


    def __password_cheker(self, name_of_app):
        if self.__password_reader(name_of_app):
            print("Thank you for using this app")
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



