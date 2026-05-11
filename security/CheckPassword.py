import random
import string
import bcrypt

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

def check_caracters_password(password):
    ascii_alphabet = string.ascii_letters
    ascii_numbers = get_ascii_numbers()
    ascii_specials_caracters = get_ascii_scpecials_caracteres()

    respect_conditions_letters = False
    respect_conditions_numbers = False
    respect_conditions_caracters = False

    for i in range (len(password)):
        for j in range (len(ascii_alphabet)):
            if(password[i] in (ascii_alphabet[j])):
                respect_conditions_letters = True

        for j in range (len(ascii_numbers)):
            if(password[i] in (ascii_numbers[j])):
                respect_conditions_numbers = True

        for j in range (len(ascii_specials_caracters)):
            if(password[i] in (ascii_specials_caracters[j])):
                respect_conditions_caracters = True

    return respect_conditions_letters and respect_conditions_numbers and respect_conditions_caracters

def check_password(user, file):
    #Demander d'entrer le mot de passe que l'on hashera ain d'enregistrer dans la base de données
    print("Voici les exemples de mot de passe à ne pas insérer :")
    print("     -0000")
    print("     -1234")
    print("     -Pas d'espace")
    print("     -Votre date de naissance")
    print("     -Un mot de passe avec une longueur de maximum 8 chaines de caractères")
    print("     -Un mot de passe avec des lettres, chiffres et caractères spéciaux")
    print("Votre mot de passe : ", end="")
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
    while check_caracters_password(password) == False:
        print("", end="\n")
        print("Votre mot de passe ne contient pas soit une lettre, soit un nombre soit un caractère spécial !")
        print("Veuillez retaper un mot de passe correct : ", end="")
        password = input()
    
    password = password.encode('UTF-8')
    salt_password = bcrypt.gensalt(12)
    hash_password = bcrypt.hashpw(password, salt_password)
    hash_password = hash_password.decode("utf-8")       #Le décode sert à enregistrer en string car sinon il y aura un double encodage.
    file.write(f"{hash_password}     {user}\n")
    print("", end="\n")