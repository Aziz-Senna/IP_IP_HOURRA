import string
import bcrypt
import datetime

class Security():

    #Obtenir la liste des caractères (lettres, nombres et speciaux) ascii
    def __get_ascii():
        ascii = []
        ascii.append(string.ascii_letters)
        
        #Obtenir la liste des nombres sours forme de chaine de caractères.
        ascii_numbers = ""
        for i in range (11):
            ascii_numbers += str(i)
        ascii.append(ascii_numbers)
        
        #Obtenir la liste des caractères spéciaux sous forme de caractères.     
        specials_caracters = ""
        for i in range(33, 47, 1):
            specials_caracters += chr(i)
        for i in range (58, 64, 1):
            specials_caracters += chr(i)
        for i in range (91, 96, 1):
            specials_caracters += chr(i)
        ascii.append(specials_caracters)
        return ascii

    @staticmethod
    def __check_caracters_password(password):
        respect_conditions_letters = False
        respect_conditions_numbers = False
        respect_conditions_caracters = False
        for i in range (len(password)):
            for j in range (len(Security.__get_ascii()[0])):
                if(password[i] in (Security.__get_ascii()[0][j])):
                    respect_conditions_letters = True

            for j in range (len(Security.__get_ascii()[1])):
                if(password[i] in (Security.__get_ascii()[1][j])):
                    respect_conditions_numbers = True

            for j in range (len(Security.__get_ascii()[2])):
                if(password[i] in (Security.__get_ascii()[2][j])):
                    respect_conditions_caracters = True
        return respect_conditions_letters and respect_conditions_numbers and respect_conditions_caracters

    @staticmethod
    def create_password():

        #Demander d'entrer le mot de passe que l'on hashera ain d'enregistrer dans la base de données    
        print("\nVeuillez choisir un mot de passe.")
        print("\nRegles a respecter : ")
        print("--------------------------------------------------------------")
        print("- Minimum 8 caracteres")
        print("- Contenir lettres + chiffres + caracteres speciaux")
        print("- Pas d'espace")
        print("- Ne pas utiliser : 0000, 1234, date de naissance (DD/MM/AAAA)")
        print("--------------------------------------------------------------")
        print("\nMot de passe : ", end="")
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

        #Verifier si le mot de passe est une date
        while Security.__is_date(password) == True:
            print("", end="\n")
            print("Vous avez entre une date !") 
            print("Veuillez retaper un mot de passe correct : ", end="")
            password = input()         

        #Vérifier si le mot contient des lettres, chiffres et caractères spéciaux
        while Security.__check_caracters_password(password) == False:
            print("", end="\n")
            print("Votre mot de passe ne contient pas soit une lettre, soit un nombre soit un caractère spécial !")
            print("Veuillez retaper un mot de passe correct : ", end="")
            password = input()
        return password
        

    #Si le mot de passe est une date
    def __is_date(string):
        try:
            date = datetime.datetime.strptime(string, "%d/%m/%Y")   #Si aucune exception n'a ete attrape alors il s'agit d'une date.
            return True
        except ValueError:
            return False

    @staticmethod    
    def write_file(password, user, file):
        file_to_write = open(file, "a")
        password = password.encode('UTF-8')
        salt_password = bcrypt.gensalt(12)
        hash_password = bcrypt.hashpw(password, salt_password)
        hash_password = hash_password.decode("utf-8")       #Le décode sert à enregistrer en string car sinon il y aura un double encodage.
        file_to_write.write(f"{hash_password}     {user}\n")
        