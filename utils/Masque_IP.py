import utils.Classe_IP

def main():
    print("Trouver le masque appartenant a l'adresse :")
    print("===========================================", end="\n")

    while True:
        ip = input("\nEntrez une adresse IP valide : ")
        parties = ip.split(".")  # car ce que l'utilisateur tape est une chaine de caractère, donc ça permet de séparer en liste
        erreurs = utils.Classe_IP.check_ip_adress(ip)

        if erreurs:
            print("\nIP invalide, erreurs détectés :")
            for erreur in erreurs:
                print(f"  - {erreur}")
            #SI BONNE IP
        else :
            if utils.Classe_IP.find_class(parties) == "A":
                print("Le masque de l'adresse IP : 255.0.0.0")

            elif utils.Classe_IP.find_class(parties) == "B":
                print("Le masque de l'adresse IP : 255.255.0.0")

            elif utils.Classe_IP.find_class(parties) == "C":
                print("Le masque de l'adresse IP : 255.255.255.0")                
            break

def transform_mask_to_binary(mask):
    binary_mask = "11111111."
    count_point = 0
    for i in range (9, 33):
        if i <= int(mask[1:]) and i % 8 != 0:
            binary_mask += "1"
        elif i <= int(mask[1:]) and i % 8 == 0 and count_point < 2:
            count_point += 1
            binary_mask += "1." 
        elif i % 8 == 0 and count_point < 2:
            count_point += 1
            binary_mask += "0." 
        elif i % 8 == 0 and count_point == 3:
            binary_mask += "0"          
        else:
            binary_mask += "0"
    return binary_mask