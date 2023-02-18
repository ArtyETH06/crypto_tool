#Cryptology tool

#Imports
import base64
import argparse
from colorama import init, Fore, Style
import codecs
from urllib.parse import quote
from urllib import *
import urllib.parse




#=================================================Arguments======================================================
#Création des arguments
if __name__ == "__main__":
    #Description globale du tool
    parser = argparse.ArgumentParser(description="Ultimate Cryptology tool (encoder/decoder)")

    #Les différents Arg
    parser.add_argument("-m", type=int, help="The mode that you want to choose")
    parser.add_argument("-c", type=str, help="The content that you want to encode/decode (can be a string or a tab)")

    #"Création" des arguments
    args = parser.parse_args()

#================================================================================================================


'''
====================================================================String --> XXX==================================================================================
=====================================================================================================================================================================
'''

#=============================================String --> Binary============================================
def string_to_binary(to_encode):
    binary = ''.join(format(ord(i), '08b') for i in to_encode)
    print(Fore.CYAN + Style.BRIGHT + "===============================================String --> Binary======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" String --> Binary\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(binary))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")
    return str(binary)
#===============================================================================================================


#=============================================String --> ROT13============================================
def string_to_rot13(to_encode):
    # Chiffrement en utilisant ROT13
    ciphertext = codecs.encode(to_encode, 'rot13')
    print(Fore.CYAN + Style.BRIGHT + "===============================================String --> ROT13======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" String --> ROT13\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(ciphertext))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")
    return str(ciphertext)
#===============================================================================================================

#===========================================String--> base64===================================================
def string_to_base64(string):
    texte_bytes = string.encode('utf-8')  # Convertir en bytes
    base64_bytes = base64.b64encode(texte_bytes)  # Encoder en base64
    base64_texte = base64_bytes.decode('utf-8')  # Convertir en chaîne de caractères
    print(Fore.CYAN + Style.BRIGHT + "===============================================String --> Base64======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" String --> Base64\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + base64_texte)
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")

#==============================================================================================================


#===========================================String --> Hexadécimal===================================================
def string_to_hexadecimal(string):
    hexa = string.encode('utf-8').hex()
    print(Fore.CYAN + Style.BRIGHT + "===============================================String --> Hexadécimal======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" String --> Hexadécimal\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + hexa)
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")

#==============================================================================================================

#===========================================String --> URL===================================================
def string_to_url(string):
    texte_encode = quote(string)
    print(Fore.CYAN + Style.BRIGHT + "===============================================String -->URL======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" String --> URL\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + texte_encode)
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")

#==============================================================================================================

#===========================================String --> ASCII===================================================
def string_to_ascii(string):
    
    texte_encode = ""

    for c in string:
        if ord(c) < 128:
            texte_encode += str(ord(c)) + " "
        else:
            texte_encode += "?"

    texte_encode = texte_encode.strip()
    print(Fore.CYAN + Style.BRIGHT + "===============================================String -->ASCII======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" String --> ASCII\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(texte_encode))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")

#==============================================================================================================

#===========================================String --> Morse===================================================
def string_to_morse(string):
    
    morse_alphabet = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
        'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
        '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '
    }

    morse = ""
    for char in string.upper():
        if char in morse_alphabet:
            morse += morse_alphabet[char] + " "
    print(Fore.CYAN + Style.BRIGHT + "===============================================String -->ASCII======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" String --> ASCII\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(morse))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")

#==============================================================================================================

'''
===========================================================================================================================================================
=====================================================================================================================================================================
'''




'''
====================================================================XXX --> String==================================================================================
=====================================================================================================================================================================
'''

#=============================================Binary --> String============================================
def binary_to_string(to_encode):
    binary_list = to_encode.split()  # Sépare la chaîne binaire en une liste de chaînes représentant chaque octet
    ascii_string = ""

    for byte in binary_list:
        decimal_value = int(byte, 2)  # Convertit l'octet binaire en une valeur décimale
        ascii_char = chr(decimal_value)  # Convertit la valeur décimale en un caractère ASCII
        ascii_string += ascii_char  # Ajoute le caractère ASCII à la chaîne résultat

    print(Fore.CYAN + Style.BRIGHT + "===============================================Binary --> String======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" Binary --> String\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(ascii_string))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")
#===============================================================================================================

#=============================================ROT13 --> String============================================
def rot13_to_string(to_encode):
    decoded_string = ""

    for char in to_encode:
        if char.isalpha():
            if char.isupper():
                decoded_char = chr((ord(char) - 65 + 13) % 26 + 65)  # Décale la lettre majuscule de 13 positions dans l'alphabet
            else:
                decoded_char = chr((ord(char) - 97 + 13) % 26 + 97)  # Décale la lettre minuscule de 13 positions dans l'alphabet
        else:
            decoded_char = char  # Garde les caractères qui ne sont pas des lettres inchangés
        decoded_string += decoded_char  # Ajoute le caractère décodé à la chaîne résultat
    print(Fore.CYAN + Style.BRIGHT + "===============================================ROT13 --> String======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" ROT13 --> String\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(decoded_string))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")
#===============================================================================================================

#=============================================Base64 --> String============================================
def base64_to_string(to_encode):
    decoded_string = base64.b64decode(to_encode).decode('utf-8')  # Décodage de la chaîne Base64, puis conversion en chaîne de caractères

    print(Fore.CYAN + Style.BRIGHT + "===============================================Base64 --> String======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" base64 --> String\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(decoded_string))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")
#===============================================================================================================

#=============================================hexadecimal --> String============================================
def hexadecimal_to_string(to_encode):
    decoded_string = bytes.fromhex(to_encode).decode('utf-8')  # Décodage de la chaîne hexadécimale, puis conversion en chaîne de caractères


    print(Fore.CYAN + Style.BRIGHT + "===============================================Hexadecimal --> String======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" Hexadecimal --> String\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(decoded_string))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")
#===============================================================================================================

#=============================================URL --> String============================================
def url_to_string(to_encode):
    decoded_string = urllib.parse.unquote(to_encode)  # Décodage de la chaîne URL


    print(Fore.CYAN + Style.BRIGHT + "===============================================URL --> String======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" URL --> String\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(decoded_string))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")
#===============================================================================================================

#=============================================ASCII --> String============================================
def ascii_to_string(to_encode):
    decoded_string = "".join(chr(int(x)) for x in to_encode.split())  # Décodage de la chaîne ASCII


    print(Fore.CYAN + Style.BRIGHT + "===============================================ASCII --> String======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" ASCII --> String\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(decoded_string))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")
#===============================================================================================================

#=============================================Morse --> String============================================
def morse_to_string(to_encode):
    morse_code = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '--..--': ',',
        '.-.-.-': '.',
        '..--..': '?',
        '-..-.': '/',
        '-....-': '-',
        '-.--.': '(',
        '-.--.-': ')',
        '.-...': '&',
        '---...': ':',
        '-.-.-.': ';',
        '-...-': '=',
        '.-.-.': '+',
        '-....-': '-',
        '..--.-': '_',
        '.-..-.': '"',
        '...-..-': '$',
        '.--.-.': '@',
        '...---...': 'SOS'
    }

    decoded_string = "".join([morse_code.get(i, ' ') for i in to_encode.split(" ")])  # Décodage de la chaîne en code Morse


    print(Fore.CYAN + Style.BRIGHT + "===============================================Morse --> String======================================\n" + Fore.GREEN + Style.BRIGHT + "Encoded_string: " + Fore.YELLOW + Style.BRIGHT + args.c + Fore.GREEN + Style.BRIGHT +"\nMethod: " + Fore.YELLOW + Style.BRIGHT +" Morse --> String\n"+ Fore.GREEN + Style.BRIGHT + "Result: " + Fore.YELLOW + Style.BRIGHT + str(decoded_string))
    print(Fore.CYAN + Style.BRIGHT +"===========================================================================================================")
#===============================================================================================================
'''
===========================================================================================================================================================
=====================================================================================================================================================================
'''



#===============================================Réalisation des fonctions========================================
#On réalise les fonctions définies plus haut
if args.m == 1:
    string_to_binary(args.c)

elif args.m == 2:
    string_to_rot13(args.c)

elif args.m == 3:
   string_to_base64(args.c)

elif args.m == 4:
    string_to_hexadecimal(args.c)

elif args.m == 5:
   string_to_url(args.c)

elif args.m == 6:
    string_to_ascii(args.c)

elif args.m == 7:
    string_to_morse(args.c)

elif args.m == 8:
    binary_to_string(args.c)

elif args.m == 9:
    rot13_to_string(args.c)

elif args.m == 10:
    base64_to_string(args.c)

elif args.m == 11:
    hexadecimal_to_string(args.c)

elif args.m == 12:
    url_to_string(args.c)

elif args.m == 13:
    ascii_to_string(args.c)

elif args.m == 14:
    morse_to_string(args.c)

#Si le mode n'est pas prit en compte
else:
    print(Fore.RED + Style.BRIGHT + "Fatal Error,mode not provided or not found")

    #==================================================================================================================