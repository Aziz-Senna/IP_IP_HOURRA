import os
import time 
import security.Login as login
import utils.Tableau_Ip as table
import utils.Classe_IP as classe
import utils.Masque_IP as masque
import utils.Network as network
from utils.Admin import Admin
from utils.User import User

def show_logo():
    print(""" 
 /$$$$$$ /$$$$$$$        /$$$$$$ /$$$$$$$        /$$   /$$  /$$$$$$  /$$   /$$ /$$$$$$$  /$$$$$$$   /$$$$$$ 
|_  $$_/| $$__  $$      |_  $$_/| $$__  $$      | $$  | $$ /$$__  $$| $$  | $$| $$__  $$| $$__  $$ /$$__  $$
  | $$  | $$  \ $$        | $$  | $$  \ $$      | $$  | $$| $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$
  | $$  | $$$$$$$/        | $$  | $$$$$$$/      | $$$$$$$$| $$  | $$| $$  | $$| $$$$$$$/| $$$$$$$/| $$$$$$$$
  | $$  | $$____/         | $$  | $$____/       | $$__  $$| $$  | $$| $$  | $$| $$__  $$| $$__  $$| $$__  $$
  | $$  | $$              | $$  | $$            | $$  | $$| $$  | $$| $$  | $$| $$  \ $$| $$  \ $$| $$  | $$
 /$$$$$$| $$             /$$$$$$| $$            | $$  | $$|  $$$$$$/|  $$$$$$/| $$  | $$| $$  | $$| $$  | $$
|______/|__/            |______/|__/            |__/  |__/ \______/  \______/ |__/  |__/|__/  |__/|__/  |__/
""")

def start_program():
    os.system("cls") 

    if login.Login.check_file("datas/admin.dat") == False:
        show_logo() 

        #Impossible de faire Admin.create_user() car la variable attend comme paramètre self. 
        admin = Admin()
        admin.create_user()
        os.system("cls")

    show_logo()
    print("PAGE D'ACCUEIL")
    print("==============", end="\n\n")
    print("Bonjour !", end="\n")
    print("Pour vous connecter en tant que :", end="\n\n")
    print("     • Administrateur    = 0")
    print("     • Utilisateur       = 1")
    print("     • Quitter           = 2", end="\n\n")
    print("Tapez : ", end="")
    choice = int(input())
    while choice < 0 or choice > 2:
        os.system("cls")
        show_logo()
        print("PAGE D'ACCUEIL")
        print("==============", end="\n\n")
        print("Bonjour !", end="\n")
        print("Pour vous connecter en tant que :", end="\n\n")
        print("     • Administrateur    = 0")
        print("     • Utilisateur       = 1")
        print("     • Quitter           = 2", end="\n\n")
        print("Tapez : ", end="")
        choice = int(input()) 
    go_to_channel(choice)

def go_to_channel(choice):
    connexion = login.Login()
    if choice == 0:
        os.system("cls")
        show_logo()
        print("CONNEXION EN TANT QU'ADMINISTRATEUR")
        print("===================================", end="\n\n")        
        connexion.login("admin")

        os.system("cls")
        show_logo()
        user = User()
        user.create_user()
        start_program()
        
    elif choice == 1 :
        os.system("cls")
        show_logo()
        print("CONNEXION EN TANT QU'UTILISATEUR")
        print("================================", end="\n")
        if connexion.check_file("datas/databases.dat") == False:
            print("Aucun utilisateur n'est inscrit.")
            print("L'administrateur doit au moins creer un compte !")
            time.sleep(2.0)
            print("\n\nTapez une touche pour revenir en arriere : ", end="")
            input()
            start_program()
        else:        
            connexion.login("user")
            choice_fonctionality()
    else:
        time.sleep(1.0)
        exit()

def choice_fonctionality():
    os.system("cls")
    show_logo()
    print("--------------------------------------------------------------")
    print("Voici les differentes fonctionalites que vous pouvez choisir : ", end="\n\n")
    print("     • (1)   Determiner la classe d'une adresse IP.")
    print("     • (2)   Determiner le masque d'une adresse IP.")
    print("     • (3)   Determiner le reseau et le sous-reseau d'une adresse IP (en classfull).")
    print("     • (4)   Determiner si deux IP sont dans le meme reseau.")
    print("     • (5)   Afficher un tableau reprenant les differentes informations sur les adresses IP.")
    print("     • (6)   Revenir a la page d'accueil.", end="\n\n")
    print("Tapez votre numero pour selectionner : ", end="")
    choice = int(input())

    while choice > 6 or choice < 1:
        print("Retapez votre numero : ", end="")
        choice = int(input())

    match choice:
        case 1:
            os.system("cls")
            classe.main()
            print("\nTapez une touche pour revenir en arriere.", end="")
            input()
        case 2:
            os.system("cls")
            masque.main()
            print("\nTapez une touche pour revenir en arriere.", end="")
            input() 
        case 3:
            os.system("cls")
            network.find_newtork_and_subnet()
            print("\nTapez une touche pour revenir en arriere.", end="")
            input()
        case 4:
            os.system("cls")
            network.compare_two_adresses()
            print("\nTapez une touche pour revenir en arriere.", end="")
            input()
        case 5:
            table.create_grid()
            print("\nTapez une touche pour revenir en arriere.", end="")
            input()
        case 6:
            os.system("cls")
            start_program()
    choice_fonctionality()
start_program()