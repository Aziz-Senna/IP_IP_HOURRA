import utils.Classe_IP
import utils.Masque_IP
import array

class Network:
    
    def __init__(self):        
        self.__ip_adress = None
        self.__network_adress = None
        self.__sub_network = None
        self.__mask = None
        self.__sub_mask = None

    def get_mask(self):
        return self.__mask
    
    def get_sub_mask(self):
        return self.__sub_mask
    
    def get_network_adress(self):
        return self.__network_adress
    
    def get_adress_sub_network(self):
        return self.__sub_network

    def get_ip_adress(self):
        return self.__ip_adress
    
    def set_mask(self, value):
        self.__mask = value

    def set_sub_mask(self, value):
        self.__sub_mask = value

    def set_adress_network(self, value):
        self.__network_adress = value

    def set_adress_sub_network(self, value):
        self.__sub_network = value
    
    def set_ip_adress(self, value):
        self.__ip_adress = value

    def split_network_into_bytes(self, adress):
        #Tranformer l'adresse IP pour avoir un vecteur de chaque octet en base 10.
        adress_int = array.array('i')
        byte = ""
        for i in range (0, len(adress)):  
            if adress[i] != ".":
                byte += adress[i]
            elif i == len(adress) or adress[i] == ".":
                adress_int.append(int(byte))
                byte = str("")
        adress_int.append(int(byte))
        return adress_int    
    
    def find_network(self):
        bytes_adress = self.split_network_into_bytes(self.get_ip_adress())
        mask = ""
        if utils.Classe_IP.find_class(bytes_adress) == "A":
            bytes_adress[1] = bytes_adress[2] = bytes_adress[3] = 0
            mask = "/8"
        elif utils.Classe_IP.find_class(bytes_adress) == "B":
            bytes_adress[2] = bytes_adress[3] = 0
            mask = "/16"
        elif utils.Classe_IP.find_class(bytes_adress) == "C":
            bytes_adress[3] = 0
            mask = "/24"
        adress_network = str(bytes_adress[0]) + "." + str(bytes_adress[1]) + "." + str(bytes_adress[2]) + "." + str(bytes_adress[3])
        self.set_mask(mask)
        return adress_network

    def find_sub_network(self, mask):
        adress_int = self.split_network_into_bytes(self.get_ip_adress())
        #Transformer chaque octet en binaire
        binary_adress = ""
        for i in range (len(adress_int)):
            number_to_cast = adress_int[i]
            for j in range (7, -1, -1):
                if number_to_cast >= pow(2,j):
                    binary_adress += "1"
                    number_to_cast -= pow(2,j)
                else :
                    binary_adress += "0"
            binary_adress += "."

        #Trouver l'adresse reseau
        #Le premier octet sera toujours reserve a la partie reseau
        network_adress_binary = str(binary_adress[0:8]) + "."
        binary_mask = utils.Masque_IP.transform_mask_to_binary(mask) 
        if int(mask[1:]) == 8:
            network_adress_binary += "00000000.00000000.00000000"
        else:
            i = 9
            while i < len(binary_mask):
                if binary_mask[i] == "1":
                    network_adress_binary += binary_adress[i] 
                elif binary_mask[i] == "0":
                    network_adress_binary += "0"
                elif binary_mask[i] == ".":    
                    network_adress_binary += "."
                i += 1

        #Transformer l'adresse reseau binaire en decimal
        network_adress_decimal = []
        for i in range(4):
            number_to_get = 0
            for j in range(8):
                if network_adress_binary[i * 9 + j] == "1":  # i*9 pour sauter les points
                    number_to_get += pow(2, 7 - j)           # 7-j pour l'exposant
            network_adress_decimal.append(str(number_to_get))

        #Permet d'afficher la liste ["192",168", "16", "2"] sous la forme d'une adresse IP. 
        return ".".join(network_adress_decimal)

    def show_treatment(self):
        self.set_adress_network(self.find_network())
        self.set_adress_sub_network(self.find_sub_network(self.get_sub_mask()))
        
        print(f"\n\nAdresse IP : {self.get_ip_adress()}")
        print(f"Adresse du réseau : {self.get_network_adress()}")
        print(f"Masque de l'adresse IP : {self.get_mask()}")
        print(f"Adresse de sous-réseau : {self.get_adress_sub_network()}")
        print(f"Masque de sous-réseau : {self.get_sub_mask()}")


def find_newtork_and_subnet():
    print("Trouver le reseau et le sous-reseau appartenant a l'adresse :")
    print("=============================================================", end="\n")
    print("Entrez votre adresse IP : ", end="")
    adress = input()
    while utils.Classe_IP.check_ip_adress(adress) != []:
        print("\nVeuillez inscrire une adresse IP valide : ", end="")
        adress = input()

    network = Network()
    network.set_ip_adress(adress)

    print("Et votre masque (en CIDR -> entre /8 et /30) : ", end="")
    mask = input()
    while len(mask) == 1 or int(mask[1:]) < 8 or int(mask[1:]) > 30:
        print("\nVeuillez taper un masque de reseau allant de /8 a /30 : ", end="")
        mask = input()
    network.set_sub_mask(mask)
    network.show_treatment() 

def compare_two_adresses():
    print("Comparer deux adresses IP avec leur masque :")
    print("============================================")
    print("Veuillez entrez votre premiere adresse IP : ", end="")
    first_adress = input()
    while utils.Classe_IP.check_ip_adress(first_adress) != []:
        print("\nVeuillez inscrire une adresse IP valide : ", end="")
        first_adress = input()
    
    print("Et votre masque (en CIDR -> entre /8 et /30) : ", end="")
    mask1 = input()
    while len(mask1) == 1 or int(mask1[1:]) < 8 or int(mask1[1:]) > 30:
        print("\nVeuillez taper un masque de reseau allant de /8 a /30 : ", end="")
        mask1 = input()

    print("\nVeuillez entrez votre deuxieme adresse IP : ", end="")
    seconde_adress = input()
    while utils.Classe_IP.check_ip_adress(seconde_adress) != []:
        print("\nVeuillez inscrire une adresse IP valide : ", end="")
        seconde_adress = input()

    print("Et votre masque (en CIDR -> entre /8 et /30) : ", end="")
    mask2 = input()
    while len(mask2) == 1 or int(mask2[1:]) < 8 or int(mask2[1:]) > 30:
        print("\nVeuillez taper un masque de reseau allant de /8 a /30 : ", end="")
        mask2 = input()
    
    network1 = Network()
    network2 = Network()
    network1.set_ip_adress(first_adress)
    network2.set_ip_adress(seconde_adress)


    network1_adress1 = network1.find_sub_network(mask1)     #Test en prenant la 1ere IP avec le premier masque
    network2_adress1 = network1.find_sub_network(mask2)     #Test en prenant la 1ere IP avec le deuxieme masque

    network1_adress2 = network2.find_sub_network(mask1)     #Test en prenant la 2e IP avec le premier masque
    network2_adress2 = network2.find_sub_network(mask2)     #Test en prenant la 2e IP avec le deuxieme masque

    print("\n----------------------------------------------------------------------------------")
    if network1_adress1 == network1_adress2:
        print("En theorie d'apres la premiere adresse Ip, les deux IP sont dans le meme reseau.")
    else:
        print("D'apres la premiere Ip, la deuxieme Ip n'est pas dans le meme reseau.")

    if network2_adress1 == network2_adress2:
        print("Selon la deuxieme adresse IP, les deux adresses sont dans le meme reseau.")
    else:
        print("D'apres la deuxieme Ip, la premiere Ip n'est pas dans le meme reseau.")        