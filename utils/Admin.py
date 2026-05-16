import time
import security.Login as log
from .UserFactory import UserFactory


class Admin(UserFactory):

    def __init__(self):
        self.__login = log.Login()

    
    def create_user(self):
        
        print("\nBienvenue chez admin !")
        print("Etant donne que le fichier 'datas/admin.dat' n'existe pas, " \
            "nous allons devoir creer un mot de passe pour le systeme d'authentification.\n\n")
        print("CREATION DE L'ADMINISTRATEUR")
        print("============================", end="\n\n")

        print("Nom d'utilisateur par defaut : root")
        password = self.__login.security.create_password()
        self.__login.security.write_file(password, "root", "datas/admin.dat")
        print("Administrateur cree !")
        time.sleep(2.0)