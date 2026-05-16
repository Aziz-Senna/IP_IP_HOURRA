import security.Login as log
from .UserFactory import UserFactory
import time

class User(UserFactory):
    
    def __init__(self):
        self.__login = log.Login()


    def create_user(self):

        print("CREATION D'UTILISATEUR")
        print("======================", end="\n\n")

        file = open("datas/databases.dat", "a")
        print("Nom d'utilisateur : ", end="")
        username = input()

        #Tant que le nom d'utilisateur entre existe deja dans la base de donnees.
        while self.__login.isExist(username) == True:
            print("Cet(te) utilisateur(trice) existe deja !\n")
            print("\nNom d'utilisateur : ", end="")
            username = input()

        password = self.__login.security.create_password()
        self.__login.security.write_file(password, username, "datas/databases.dat")
        file.close()
        print("Utilisateur cree !")
        time.sleep(2.0)