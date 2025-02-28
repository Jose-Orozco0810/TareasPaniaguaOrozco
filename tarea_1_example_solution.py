import re

#Separa las letras mayusculas y minusculas
def separador(separa_letras):
    Mayusculas = "".join([M for M in separa_letras if M.isupper()])
    Minusculas = "".join([M for M in separa_letras if M.islower()])
    return Mayusculas, Minusculas

#Toma los datos
#print("La siguiente cadena de caracteres debe seguir las siguientes reglas:")
#print("1. La cadena debe ser un string.")
#print("2. Solo debe contener letras del abecedario.")
#print("3. La cadena no puede estar vacia, esto icluye los espacios.")
Cadena = input("Ingrese la cadena de caracteres:")

def separar_letras(Cadena):
    #Comprueba que la entrada sea un string
    if(not bool(re.search(r"\d", Cadena))):
        #Comprueba si tiene caracteres que no sean del abecedario.
        if (bool(re.fullmatch(r"[A-Za-z ]+", Cadena))):
            #Comprueba si el string esta vacio.
            if(bool(Cadena) and Cadena.strip()):
                print("Código de Exito 0. La separacion se realizo de manera exitosa.")
                mayusculas, minusculas =separador(Cadena)
                print(mayusculas)
                print(minusculas)
            else:
                print("Código de Error -300. La cadena no puede estar vacia.")
                print("None")
                print("None")
        else:
            print("Código de Error -200. La cadena posee caracteres que no son del abecedario.")
            print("None")
            print("None")

    else:
        print("Código de Error -100. La cadena no debe tener numeros.")
        print("None")
        print("None")

separar_letras(Cadena)
