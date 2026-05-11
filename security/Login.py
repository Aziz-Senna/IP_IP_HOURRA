import security.CheckPassword as CheckPassword
import bcrypt
import time
import os
    
#Vérifier si la base de données existe, si elle n'existe pas alors elle sera crée.
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
        return True
    else:
        file = open(file, "a")
        return False


def create_administrator(datas):
    file = open(datas, "w")
    #Demander le nom d'utilisateur de l'admin
    print("Bonjour ! ")
    print("Votre nom d'administrateur par défault est root.")
    CheckPassword.check_password("root", file)
    print("Administrateur crée !")
    time.sleep(2.0)

def create_user(database):
    if check_file(database) == True:
        file = open(database, "a")
        print("Nom d'utilisateur : ", end="")
        user = input()
        CheckPassword.check_password(user, file)
    else :  #Si le fichier comprenant le nom des users et mdp n'existe alors on le crée puis on réappelle la méthode.        
        create_user(database)
        print("")
    print("Utilisateur crée !")
    time.sleep(2.0)


def login_admin():
    print("Nom d'administrateur : ", end="")
    admin = input()

    print(f"Mot de passe : ", end="")
    password = input()
    global_login(admin, password, "datas/admin.dat")
    

def login_user():
    if check_file("datas/databases.dat") == False:
        print("Aucun utilisateur n'est inscrit.")
        print("Vous devez donc créer un compte !")
        time.sleep(2.0)
        create_user("datas/databases.dat")
        os.system("cls")
        print("CONNEXION EN TANT QU'UTILISATEUR")
        print("================================", end="\n")
    
    print("", end="\n")
    print("Nom d'utilisateur : ", end="")
    user = input()
    print("Mot de passe : ", end="")
    password = input()
    global_login(user, password, "datas/databases.dat")


def global_login(user, password, file):
    password = password.encode("utf-8")
    file_to_read = open(file, "r")
    if file == "datas/databases.dat":
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
            if col2 == user :
                col1 = col1.encode("utf-8")
                if bcrypt.checkpw(password, col1) == True:
                    print("Connexion réussie !")
                    time.sleep(2.0)
                    print("\n\n")
                else :
                    print(f"Mot de passe incorrect !\n")
                    file_to_read.close()
                    login_user()
                break


            elif col2 != user and num_line_user == nb_lines_total:
                print("Nom d'utilisateur incorrect !", end="\n")
                file_to_read.close()
                login_user()
            else :
               num_line_user = num_line_user + 1 
        else :
            print("Nom d'utilisateur incorrect !")
            file_to_read.close()
            login_user()
    
    elif file == "datas/admin.dat":
        #Lire les deux colonnes du fichier
        for line in file_to_read:
            col1, col2 = line.split()

        col1 = col1.encode("utf-8")     #Encoder le hash en octet car la fonction bcrypt.chechpw ne comprend pas les string

        #Comparer les données avec les entrées de l'admin
        if user == col2:
            if bcrypt.checkpw(password, col1) == True:
                print("Connexion réussie !")
                time.sleep(2.0)
                print("\n\n")
            else :
                print(f"Mot de passe incorrect !\n")
                file_to_read.close()
                login_admin()
        else :
            print(f"Mot de passe incorrect !\n")
            file_to_read.close()
            login_admin()