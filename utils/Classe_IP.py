def main():
    print("Trouver la classe de l'adresse IP :")
    print("===================================", end="\n")
    while True:
        ip = input("\nEntrez une adresse IP valide : ")
        parties = ip.split(".")  # car ce que l'utilisateur tape est une chaine de caractère, donc ça permet de séparer en liste
        erreurs = check_ip_adress(ip)

        if erreurs:
            print("\nIP invalide, erreurs détectés : ")
            for erreur in erreurs:
                print(f"  - {erreur}")
        #SI BONNE IP 
        else:
            print("\nIP valide !")
            if find_class(parties) == "A" :
                print("Votre IP se trouve dans la classe A")

            elif find_class(parties) == "B" :
                print("Votre IP se trouve dans la classe B")

            elif find_class(parties) == "C" : 
                print("Votre IP se trouve dans la classe C")
                
            elif find_class(parties) == "D" :
                print("Votre IP se trouve dans la classe D")

            elif find_class(parties) == "E" :
                print("Votre IP se trouve dans la classe E") 

            #SI C'est une adresse réservée 
            if int(parties[0])==127:
                print ("Ceci est une adresse réservée, elle appartient donc à aucune classe") 
    
            #SI C'EST UNE IP PRIVEE
            if int(parties[0])==10 or (int(parties[0])== 172 and 16<=int(parties[1])<=31) or (int(parties[0])== 192 and int(parties[1])==168):
                print("Ceci est une IP privée")
                

            break  # on sort de la boucle si l'IP est valide

def find_class(parties):
    #déterminer la classe de l'ip rentrée 
    if 1<=int (parties[0])<=127 :
        return "A"

    elif 128<= int(parties[0])<=191:        
        return "B"
    
    elif 192<= int(parties[0])<=223:
        return "C"
    
    elif 224<= int(parties[0])<=239:        
        return "D" 
    
    elif 240<= int(parties[0])<=255:
        return "E"
    
    

def check_ip_adress(adress_ip):
    parties = adress_ip.split(".")  # car ce que l'utilisateur tape est une chaine de caractère, donc ça permet de séparer en liste
    erreurs = []  # tableau pour mettre les erreurs dedans

    # vérification que l'adresse IP encodé est dans le bon format 1111.1111.1111.1111
    # condition 1: L'IP encodé doit être séparé de 3 POINTS
    # condition 2 : L'IP ne doit PAS contenir de lettres ou caractères autre que les 4 points et chiffres sinon --> pas bon
    # condition 3 : chaque octets doit être un nombre entre 0 et 255(en binaire) sinon --> pas bon

    # CONDITIONS POUR QUE CA SOIT PAS BON :

    # vérifier que l'IP encodé contient bien 3 points
    if adress_ip.count(".") != 3:
        erreurs.append("L'IP doit contenir 3 points.")
    # vérifier que l'IP a bien 4 parties
    if len(parties) != 4:
        erreurs.append("L'IP doit contenir 4 parties.")
    # vérifier que l'IP ne contient QUE des nombres
    for i, partie in enumerate(parties):
        if not partie.isdigit():
            erreurs.append(f"La partie {i+1} ('{partie}') n'est pas valide.")
        #si il y a bien que des nombres 
        else:
            #vérifier que les nombres tapés soient entre 0 et 255
            if int(partie) < 0 or int(partie) > 255:
                # conversion en binaire du nombre tapé
                erreurs.append(f"La partie {i+1} ({partie} = {bin(int(partie))}) doit être entre 0 (00000000) et 255 (11111111).")
    return erreurs