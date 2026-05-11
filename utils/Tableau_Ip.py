import pandas as pd
import os

def create_grid():
    os.system("cls")
    print("TABLEAU AVEC LES DIFFERENTES INFORMATIONS SUR LES IP")
    print("====================================================", end="\n\n")
    print("Notation CIDR               Binaire                           Décimal    Masque", end="\n")
    datas = pd.read_csv('datas/tableau_ip.csv', sep=';', encoding='latin-1')       
    #Appeler le fichier csv qui contient les données du tableau, latin-1 pour accepter les accents et skiprows pour ignorer la première ligne du fichier csv
    
    datas = datas[["Notation CIDR", "Binaire", "Décimal", "Masque"]]    
    #Sélectionner les colonnes qui m'interessent dans le fichier csv
    
    datas = datas.to_string(index=False, header=False)                                
    #Ne pas afficher le numéro des lignes et ne pas afficher les colonnes    
    print(datas)