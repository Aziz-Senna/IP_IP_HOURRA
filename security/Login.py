import security.Security as secu
import bcrypt
import time
import os

class Login:

    def __init__(self):
        self.__nb_fails_password = 0
        self.__username = None
        self.__type_user = None
        self.__file = None
        self.security = secu.Security()

    def get_username(self):
        return self.__username
    
    def set_username(self, string):
        self.__username = string

    def get_type_user(self):
        return self.__type_user
    
    def set_type_user(self, string):
        self.__type_user = string

    def get_file(self):
        return self.__file
    
    def set_file(self, path):
        self.__file = path

    def increment_fails_connexion(self):
        if self.__nb_fails_password == 2:
            self.__nb_fails_password = 0
            self.change_forgotten_password()
        else:
            self.__nb_fails_password = self.__nb_fails_password + 1


    def change_forgotten_password(self):
        print("\n\nSouhaitez-vous changer votre mot de passe (0/1) ? ", end="")
        confirm = int(input())
        while confirm != 0 and confirm != 1:
            print("Veuillez choix entre 0 et 1 !")
            print("Souhaitez-vous changer votre mot de passe (0/1) ? ", end="")
            confirm = int(input())

        if confirm == 0:
            return
        elif confirm == 1:
            os.system("cls")
            print("Changement du mot de passe")
            print("------------------------------------------------")
            print(f"\n\nNom d'utilisateur : {self.get_username()}")
            new_password = self.security.create_password()

            if self.get_type_user() == "user":
                # Lire tout le contenu du fichier
                with open(self.get_file(), "r") as f:
                    lines = f.readlines()

                # Chercher l'ancien mot de passe
                old_password = ""
                if self.get_file() == "datas/databases.dat":
                    for line in lines:
                        col1, col2 = line.split()
                        if col2 == self.get_username():
                            old_password = col1
                            break

                # Supprimer la ligne correspondant à l'utilisateur
                ligne = old_password + "     " + self.get_username()
                with open(self.get_file(), "w") as f:
                    for line in lines:
                        if line.strip("\n") != ligne:
                            f.write(line)
            
            else:   #Car il fait un doublon de root dans le fichier. J'ecrase le contenu puisqu'il n'y a qu'une ligne.
                open(self.get_file(), "w").close()  
                self.set_file("datas/admin.dat")
                self.set_username("root")

            # Ecrire les nouvelles donnees a la fin du fichier
            self.security.write_file(new_password, self.get_username(), self.get_file())
            
            #Revenir en arriere
            print("Changement de mot de passe effectue ! ")
            time.sleep(1.0)
            os.system("cls")

            #Si c'est l'admin qui a change son mdp, sinon c'est un utilisateur.
            if self.get_type_user() == "admin":
                print("CONNEXION EN TANT QU'ADMINISTRATEUR")
                print("===================================", end="\n\n") 
            else:
                print("CONNEXION EN TANT QU'UTILISATEUR")
                print("================================", end="\n")    
            return 

    
    
    #Vérifier si la base de données existe, si elle n'existe pas alors elle sera crée.
    @staticmethod
    def check_file(file):
        exists = False
        try:
            with open(file,"r") as f:
                exists = True
        except FileNotFoundError as e:
            exists = False
        except IOError as e:
            exists = False
        
        if exists == True:
            if os.path.getsize(file) == 0:      #Si le fichier existe mais qu'il est vide alors on le supprime.
                os.remove(file)
                return False
            else:            
                return True
        else:
            return False
        
    def create_administrator(self, datas):
        print("Nom d'utilisateur par defaut : root")
        password = self.security.create_password()
        self.security.write_file(password, "root", datas)
        print("Administrateur cree !")
        time.sleep(2.0)

    def create_user(self, database):
        if self.check_file(database) == False:
            open(database, "w").close()  # Creer le fichier puis le fermer afin qu'il soit vide et creer des users.
        
        file = open(database, "a")
        print("Nom d'utilisateur : ", end="")
        username = input()

        #Tant que le nom d'utilisateur entre existe deja dans la base de donnees.
        while self.isExist(username) == True:
            print("Cet(te) utilisateur(trice) existe deja !\n")
            print("\nNom d'utilisateur : ", end="")
            username = input()

        password = self.security.create_password()
        self.security.write_file(password, username, database)
        file.close()
        print("Utilisateur cree !")
        time.sleep(2.0)

    #Si l'utilisateur existe deja dans la base de donnees.
    def isExist(self, username):
        username = username
        #Trouver la ligne ou le nom de l'utilisateur est inscrit
        file_to_read = open("datas/databases.dat", "r")
        for line in file_to_read:
            col1, col2 = line.split()
            if col2 == username :
                return True
        return False


    def start_login(self, type_of_login):
        type_of_login = str(type_of_login).lower()
        self.set_type_user(type_of_login)
        if type_of_login == "admin":
            print("Nom d'administrateur : ", end="")
            self.set_username(input())
            print("Mot de passe : ", end="")
            password = input()
            self.set_file("datas/admin.dat")
            self.login(password)

        elif type_of_login == "user":
            print("", end="\n")
            print("Nom d'utilisateur : ", end="")
            username = input()
            print("Mot de passe : ", end="")
            password = input()
            self.set_username(username)
            self.set_file("datas/databases.dat")
            self.login(password)    

    def login(self, password):
        password = password.encode("utf-8")
        file_to_read = open(self.get_file(), "r")
        if self.get_file() == "datas/databases.dat":
            #Avoir le nombre de lignes dans le fichier
            nb_lines_total = 0
            for line in file_to_read:
                nb_lines_total = nb_lines_total + 1

            #On revient tout en haut du fichier pour la lecture car on est déjà à la fin
            file_to_read.seek(0)
            
            #Trouver la ligne où le nom de l'utilisateur est inscrit
            num_line_user = 0
            for line in file_to_read:
                col1, col2 = line.split() 
                if col2 == self.get_username() :
                    col1 = col1.encode("utf-8")
                    if bcrypt.checkpw(password, col1) == True:
                        print("Connexion réussie !")
                        time.sleep(2.0)
                        print("\n\n")
                    else :
                        print(f"Mot de passe incorrect !")
                        self.increment_fails_connexion()
                        file_to_read.close()
                        self.login("user")
                    break

                elif col2 != self.get_username() and num_line_user == nb_lines_total:
                    print("Nom d'utilisateur incorrect !", end="\n")
                    file_to_read.close()
                    self.start_login("user")
                else :
                    num_line_user = num_line_user + 1 
            else :
                print("Nom d'utilisateur incorrect !")
                file_to_read.close()
                self.start_login("user")
        
        elif self.get_file() == "datas/admin.dat":
            #Lire les deux colonnes du fichier
            for line in file_to_read:
                col1, col2 = line.split()

            col1 = col1.encode("utf-8")     #Encoder le hash en octet car la fonction bcrypt.chechpw ne comprend pas les string

            #Comparer les données avec les entrées de l'admin
            if self.get_username() == col2:
                if bcrypt.checkpw(password, col1) == True:
                    print("Connexion réussie !")
                    time.sleep(2.0)
                else :
                    print(f"Mot de passe incorrect !\n")
                    self.increment_fails_connexion()
                    file_to_read.close()
                    self.start_login("admin")
            else :
                print(f"Mot de passe incorrect !\n")
                self.increment_fails_connexion()
                file_to_read.close()
                self.start_login("admin")

