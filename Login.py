import bcrypt
import string

class Connexion():
    
    #Vérifier si la base de données existe, si elle n'existe pas alors elle sera crée.
    def verifier_bd(file):
        exists = False
        try:
            with open(file,"r") as f:
                exists = True
        except FileNotFoundError as e:
            exists = False
        except IOError as e:
            exists = False
        
        if exists == True:
            return print("Ce fichier existe déjà !")
        else:
            file = open(file, "w")
            return print("Fichier crée avec succès !")
        





    def creer_administrateur(base_de_donnees):
        #Demander le nom d'utilisateur de l'admin
        print("Bonjour ! ")
        print("Afin de créer un administrateur pour cette base de données, veuillez entrer un nom d'utilisateur :", end="\n")  
        user = input()

        #Demander d'entrer le mot de passe que l'on hashera ain d'enregistrer dans la base de données
        print("", end="\n\n")
        print("Et veuillez entrer un mot de passe sécurisé.")
        print("Voici les exemples de mot de passe à ne pas insérer :")
        print("-0000    -1234")
        print("-Pas d'espace")
        print("-Votre date de naissance     -Un mot de passe avec une longueur de maximum 8 chaines de caractères")
        print("-Un mot de passe avec des lettres, chiffres et caractères spéciaux")
        password = input()

        #Vérifier la longueur du mot de passe
        while len(password) <= 8:
            print("", end="\n")
            print("Votre mot de passe est trop court !")
            print("Veuillez retaper un mot de passe correct : ", end="")
            password = input()

        #Vérifier si le mot de passe n'est pas 0000 ou 1234
        while password == "1234" or password == "0000":
            print("", end="\n")
            print("Votre mot de passe ne doit pas être 0000 ou 1234 !")
            print("Veuillez retaper un mot de passe correct : ", end="")
            password = input()

        #vérifier si le mot de passe contient un espace
        space_contains = False
        for i in range (len(password)):
            if(password[i] == chr(32)):
                space_contains = True
        while space_contains == True:
            print("", end="\n")
            print("Votre mot de passe ne doit pas contenir un espace !")
            print("Veuillez retaper un mot de passe correct : ", end="")
            password = input() 
            space_contains = False
            for i in range (len(password)):
                if(password[i] == chr(32)):
                    space_contains = True            

        #Vérifier si le mot contient des lettres, chiffres et caractères spéciaux
        ascii_alphabet = string.ascii_letters
        ascii_numbers = Connexion.get_ascii_numbers()
        ascii_specials_caracters = Connexion.get_ascii_scpecials_caracteres()
        for i in range (len(password)):
            respect_conditions_letters = False
            respect_conditions_numbers = False
            respect_conditions_caracters = False
            
            #Vérifier à partir de la liste des lettres
            




    #Obtenir la liste des nombres sours forme de chaine de caractères.
    def get_ascii_numbers():
        txt = ""
        for i in range (11):
            txt += str(i)
        return txt

    #Obtenir la liste des caractères spéciaux sous forme de caractères.    
    def get_ascii_scpecials_caracteres():
        txt = ""
        for i in range(33, 47, 1):
            txt += chr(i)
        for i in range (58, 64, 1):
            txt += chr(i)
        for i in range (91, 96, 1):
            txt += chr(i)
        return txt